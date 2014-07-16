from storages.backends.s3 import S3Storage

StaticS3Storage = lambda: S3Storage(location='static')
MediaS3Storage = lambda: S3Storage(location='media')
