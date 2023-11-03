from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from courses.models import Course
from .serializers import CourseSerializer, CourseStudentSerializer
from accounts.permission import IsSuperUser, IsSuperUserOrAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        else:
            return Course.objects.filter(students=self.request.user)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsSuperUserOrAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"


class StudentsCoursesView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    serializer_class = CourseStudentSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"
