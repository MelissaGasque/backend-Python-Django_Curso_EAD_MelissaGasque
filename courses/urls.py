from django.urls import path
from .views import CourseView, CourseDetailView, StudentsCoursesView


urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<course_id>/", CourseDetailView.as_view()),
    path("courses/<course_id>/students/", StudentsCoursesView.as_view()),
]
