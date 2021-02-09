from django.urls import path

from .views import MarksManager, BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('<str:slug>_marks/', MarksManager.as_view(), name='discipline_marks'),
]
