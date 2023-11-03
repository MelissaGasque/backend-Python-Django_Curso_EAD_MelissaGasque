from django.db import models
from uuid import uuid4 as v4


class STUDENT_COURSE_STATUS(models.TextChoices):
    PENDING = "pending",
    ACCEPTED = "accepted",


class StudentCourse(models.Model):
    id = models.UUIDField(default=v4, editable=False, primary_key=True)
    status = models.CharField(
        choices=STUDENT_COURSE_STATUS.choices,
        default=STUDENT_COURSE_STATUS.PENDING
    )
    course = models.ForeignKey(
        "courses.Course",
        related_name="students_courses",
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        "accounts.Account",
        related_name="students_courses",
        on_delete=models.CASCADE,
    )
