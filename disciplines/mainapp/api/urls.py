from django.urls import path

from .api_views import (
    DisciplineListAPIView,
    GroupListAPIView,
    StudentListAPIView,
    MarkAPIView,
    TeacherListAPIView,
    StudentRetrieveAPIView,
)


urlpatterns = [
    path('disciplines/', DisciplineListAPIView.as_view(), name='disciplines'),
    path('groups/', GroupListAPIView.as_view(), name='groups'),
    path('marks/<str:id>/', MarkAPIView.as_view(), name='marks'),
    path('marks/', MarkAPIView.as_view(), name='marks'),
    path('teachers/', TeacherListAPIView.as_view(), name='teachers'),
    path('students/<str:id>/', StudentRetrieveAPIView.as_view(), name='students'),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
]
