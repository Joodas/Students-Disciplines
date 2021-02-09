from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg

from .models import Mark, Discipline, Group


class BaseView(View):
    def get(self, request):
        disciplines = Discipline.objects.all()
        groups = Group.objects.all()
        context = {
            'disciplines': disciplines,
            'groups': groups,
        }
        return render(request, 'base.html', context)


class MarksManager(View):
    @staticmethod
    def get(request, **kwargs):
        discipline_slug = kwargs.get('slug')
        discipline = Discipline.objects.get(slug=discipline_slug)
        marks = Mark.objects.filter(discipline=discipline)
        avg_marks = Mark.objects.filter(discipline=discipline).aggregate(Avg('mark'))
        context = {
            'marks': marks,
            'avg_marks': avg_marks,
        }
        return render(request, 'discipline_marks.html', context)
