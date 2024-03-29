from django.urls import path
from .views import ContentView, ContentCourse


urlpatterns = [
    path("courses/<course_id>/contents/", ContentView.as_view()),
    path("courses/<course_id>/contents/<content_id>/", ContentCourse.as_view()),
]
