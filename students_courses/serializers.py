from rest_framework import serializers
from .models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username')
    student_email = serializers.EmailField(source='student.email')

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]