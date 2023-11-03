from django.db import models
from uuid import uuid4 as v4


class Content(models.Model):
    id = models.UUIDField(default=v4, editable=False, primary_key=True)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(
        "courses.Course",
        related_name="contents",
        on_delete=models.CASCADE,
    )

