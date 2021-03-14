from django.urls import path

from .api_views import DisciplineListAPIView, GroupListAPIView, StudentListAPIView, MarkListAPIView


urlpatterns = [
    path('disciplines/', DisciplineListAPIView.as_view(), name='disciplines'),
    path('group/', GroupListAPIView.as_view(), name='group'),
    path('student/', StudentListAPIView.as_view(), name='student'),
    path('mark/', MarkListAPIView.as_view(), name='mark'),
]
