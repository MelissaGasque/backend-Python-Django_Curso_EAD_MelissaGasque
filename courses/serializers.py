from rest_framework import serializers
from accounts.models import Account
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        exclude = ['students']
        extra_kwargs = {
            'id': {'read_only': True},
            'status': {'read_only': True},
        }


class CourseStudentSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses"
        ]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance, validated_data):
        students_found = []
        emails_not_found = []

        for student in validated_data["students_courses"]:
            estudante = student["student"]
            estudante_verificado = Account.objects.filter(email=estudante["email"]).first()
            if estudante_verificado:
                students_found.append(estudante_verificado)
            else:
                emails_not_found.append(estudante["email"])

        if students_found:
            instance.students.add(*students_found)
            return instance
        else:
            error_message = f"No active accounts was found: {', '.join(emails_not_found)}."
            raise serializers.ValidationError({"detail": error_message})