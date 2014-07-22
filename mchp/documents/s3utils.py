from storages.backends.s3 import S3Storage

import base64
import hmac
import hashlib
import time
import magic
import urllib.parse

StaticS3Storage = lambda: S3Storage(location='static')
MediaS3Storage = lambda: S3Storage(location='media')

def filetype(loc):
    mime = magic.Magic(mime=True)
    print(mime.from_file(loc))

class S3Auth:

    def __init__(self, access, secret, AWS_region='us-east-1'):
        self.AWS_ACCESS_KEY_ID = access
        self.AWS_SECRET_ACCESS_KEY = secret
        self.AWS_region = AWS_region

    def get_v2(self, bucket, key, expire=30):
        expires = int(time.time()) + expire
        StringToSign = "GET" + "\n" +\
                "\n" +\
                "\n" +\
                str(expires) + "\n" +\
                '/'+bucket+key
        sig = hmac.new(self.encode(self.AWS_SECRET_ACCESS_KEY), msg=self.encode(StringToSign),
                       digestmod='sha1').digest()
    
        base_url = '{}.s3.amazonaws.com'.format(bucket)
        sig = base64.b64encode(sig).decode()
        parms = [
            ('AWSAccessKeyId', self.AWS_ACCESS_KEY_ID),
            ('Expires', expires),
            ('Signature', sig),
        ]
        encoded_parms = urllib.parse.urlencode(parms)
        url = 'https://' + base_url + '{}?{}'.format(key, encoded_parms)
        return url

    # this one doesn't work 
    def get_v4(self, bucket, key):
        base_url = '{}.s3.amazonaws.com'.format(bucket)
        resource_url = key
        cred = self.AWS_ACCESS_KEY_ID + '/' + time.strftime("%Y%m%d")+ '/' + self.AWS_region + '/' + 's3' + '/' + 'aws4_request'
        date = time.strftime('%Y%m%dT000000Z')
        expires = 604700
        headers = 'host'

        parms = [
            ('X-Amz-Algorithm', 'AWS4-HMAC-SHA256'), 
            ('X-Amz-Credential', cred),
            ('X-Amz-Date', date),
            ('X-Amz-Expires', expires),
            ('X-Amz-SignedHeaders', headers),
        ]
        encoded_parms = urllib.parse.urlencode(parms)

        canonical_request = 'GET\n' +\
                resource_url + '\n' +\
                encoded_parms + '\n' +\
                'host' + ':' + base_url + '\n\n' +\
                'host' + '\n' +\
                'UNSIGNED-PAYLOAD'
        canonical_bytes = hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
        scope = time.strftime('%Y%m%d') + '/' + self.AWS_region + '/s3/aws4_request' 
        string_to_sign = 'AWS4-HMAC-SHA256' + '\n' +\
                date + '\n' +\
                scope + '\n' +\
                canonical_bytes
        # print(canonical_request)
        # print(string_to_sign)

        date_key = hmac.new(b"AWS4" + self.encode(self.AWS_SECRET_ACCESS_KEY),
                            msg=self.encode(time.strftime('%Y%m%d')),
                            digestmod=hashlib.sha256).digest()
        date_region_key = hmac.new(date_key, 
                                   msg=self.encode(self.AWS_region),
                                   digestmod=hashlib.sha256).digest()
        date_region_service_key = hmac.new(date_region_key, 
                                           msg=b"s3",
                                           digestmod=hashlib.sha256).digest()
        signing_key = hmac.new(date_region_service_key, 
                               msg=b'aws4-request',
                               digestmod=hashlib.sha256).digest()
        sig = hmac.new(signing_key, 
                       msg=self.encode(string_to_sign), 
                       digestmod=hashlib.sha256).digest()
        import base64
        sig = base64.b64encode(sig).decode()
        url = 'https://' + base_url + '{}?{}&{}'.format(key, encoded_parms,
                                                           urllib.parse.urlencode({
                                                               'X-Amz-Signature': sig
                                                           }))

        return url

    def encode(self, string):
        return string.encode('utf-8')
