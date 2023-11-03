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
        list_students = []
        list_emails = []

        for student in validated_data["students_courses"]:
            estudante = student["student"]
            estudante_encontrado = Account.objects.filter(email=estudante["email"]).first()
            if estudante_encontrado:
                list_students.append(estudante_encontrado)
            else:
                list_emails.append(estudante["email"])
        if list_emails:
            raise serializers.ValidationError({"detail": f"No active accounts was found: {', '.join(list_emails)}."})
        if not self.partial:
            instance.students.add(*list_students)
            return instance
        return super().update(instance, validated_data)
