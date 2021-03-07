from django.urls import path

from .views import BaseView, MarksManagerByDiscipline, MarksManagerByGroup

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('<str:slug>_marks/', MarksManagerByDiscipline.as_view(), name='discipline_marks'),
    path('group_<str:slug>/', MarksManagerByGroup.as_view(), name='group_marks'),
]
