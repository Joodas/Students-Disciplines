from django.urls import path

from .api_views import (
    DisciplineListAPIView,
    GroupListAPIView,
    StudentListAPIView,
    MarkListAPIView,
    TeacherListAPIView,
    PostgraduateListAPIView,
    StudentRetrieveAPIView,
)


urlpatterns = [
    path('disciplines/', DisciplineListAPIView.as_view(), name='disciplines'),
    path('group/', GroupListAPIView.as_view(), name='group'),
    path('student/', StudentListAPIView.as_view(), name='student_list'),
    path('mark/', MarkListAPIView.as_view(), name='mark'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher'),
    path('postgraduate/', PostgraduateListAPIView.as_view(), name='postgraduate'),
    path('student/<str:id>/', StudentRetrieveAPIView.as_view(), name='student'),
]
