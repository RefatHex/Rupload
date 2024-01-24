import os
from uuid import uuid4
from django.db import models
import uuid


class Folder(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)


def get_upload_path(insatance, filename):
    return os.path.join(str(insatance.folder.uuid), filename)


class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now=True)
