from django.db import IntegrityError

class DuplicateFileError(IntegrityError):
    pass
