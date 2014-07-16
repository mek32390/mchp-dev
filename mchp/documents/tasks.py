from __future__ import absolute_import

from celery import shared_task

from django.conf import settings

import subprocess
from wand.image import Image
import urllib
import logging
logger = logging.getLogger(__name__)

@shared_task
def create_preview(instance):
    size = 500 
    name = instance.preview 

    response = urllib.request.urlopen(instance.document.url)
    urllib.request.urlretrieve(instance.document.url, '/tmp/tmp.pdf')
    try:
        with Image(filename='/tmp/tmp.pdf[0]') as img:
            preview_name = '/tmp/what.png'
            img.save(filename=preview_name)
            img = Image(filename=preview_name)
            img.transform(resize=str(size))
            img.save(filename=preview_name)

            acl = '--acl public-read'
            command = 'aws s3 cp {} s3://{}/media/{} {}'.format(preview_name,
                                                                settings.AWS_STORAGE_BUCKET_NAME,
                                                                name, acl)
            logger.debug(command)
            _run(command)
    finally:
        response.close()

    # logger.debug(instance.filetype)
    # logger.debug(instance.document)
    # tmp_name = 'tmp.pdf'
    # unoconv_command = 'unoconv -f pdf -e PageRange=1 --output="{}{}" "{}{}" && '.format(
    #     settings.MEDIA_URL,
    #     tmp_name,
    #     settings.MEDIA_URL,
    #     instance.document,
    # ) + "convert -thumbnail {} -background\
    #         white {}{}[0] {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             tmp_name,
    #             settings.MEDIA_URL, 
    #             name)

    # pdf_command = "convert -thumbnail {} -background\
    #         white {}{}[0] {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             instance.document, 
    #             settings.MEDIA_URL, 
    #             name)

    # pic_command = "convert -thumbnail {} -background\
    #         white {}{} {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             instance.document, 
    #             settings.MEDIA_URL, 
    #             name)

    # empty_command = ''

    # command = {
    #     b'application/pdf': pdf_command,
    #     b'application/msword': unoconv_command,
    #     b'text/plain': unoconv_command,
    #     b'application/vnd.openxmlformats-officedocument.wordprocessingml.document': unoconv_command,

    #     # TODO: the normal pics can just use a pic.thumbnail function call i think
    #     b'image/jpg': pic_command,
    #     b'image/png': pic_command,
    #     # gifs have multiple 'pages' (frames)
    #     b'image/gif': pdf_command,
    #     }.get(instance.filetype, empty_command)

    # _convert(command)

# just runs the command passed to it
def _run(command):
    logger.debug(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_value = proc.communicate()[0]
    logger.debug('stdout: ' + str(stdout_value))
