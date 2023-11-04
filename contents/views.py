from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.permission import IsSuperUser, IsSuperUserOrAuthenticated
from .serializers import ContentSerializer
from .models import Content
from courses.models import Course
from rest_framework.exceptions import NotFound
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course_id = self.kwargs.get(self.lookup_url_kwarg)
        course = Course.objects.get(id=course_id)
        if not course:
            raise NotFound({'detail': 'course not found.'})
        serializer.save(course=course)


class ContentCourse(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrAuthenticated]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_id"

    def get_object(self):
        course_id = self.kwargs.get("course_id")
        content_id = self.kwargs.get("content_id")

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise NotFound({'detail': 'course not found.'})

        if not self.request.user.is_superuser:
            list_students = course.students.all()
            if self.request.user not in list_students:
                raise PermissionDenied()

        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            raise NotFound({'detail': 'content not found.'})

        return content

    def get_queryset(self):
        return Content.objects.filter(id=self.kwargs.get(self.lookup_url_kwarg))
