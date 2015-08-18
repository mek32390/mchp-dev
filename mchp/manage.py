#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mchp.settings")

    max_bg_images = os.popen('ls lib/static/lib/img/bgimages/bg-*.jpeg | wc -l').read().strip()
    os.environ.setdefault("MAX_BG_IMAGES", max_bg_images)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
