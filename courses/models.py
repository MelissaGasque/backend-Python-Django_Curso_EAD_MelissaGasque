from django.db import models
from uuid import uuid4 as v4


class COURSE_STATUS(models.TextChoices):
    NOT_STARTED = "not started",
    IN_PROGRESS = "in progress",
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(default=v4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    status = models.CharField(
        max_length=11,
        choices=COURSE_STATUS.choices,
        default=COURSE_STATUS.NOT_STARTED
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        related_name="courses",
        on_delete=models.CASCADE,
        null=True
    )
    students = models.ManyToManyField(
        "accounts.Account",
        related_name='my_courses',
        through="students_courses.StudentCourse",
    )
