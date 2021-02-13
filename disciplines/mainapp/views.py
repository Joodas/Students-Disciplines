from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg

from .models import Mark, Discipline, Group, Student


class BaseView(View):
    def get(self, request):
        disciplines = Discipline.objects.all()
        groups = Group.objects.all()
        context = {
            'disciplines': disciplines,
            'groups': groups,
        }
        return render(request, 'base.html', context)


class MarksManagerByDiscipline(View):
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


class MarksManagerByGroup(View):
    @staticmethod
    def get(request, **kwargs):
        group_slug = kwargs.get('slug')
        group = Group.objects.get(slug=group_slug)
        students = Student.objects.filter(group=group)
        mark = []
        for student in students:
            mark_ = Mark.objects.get(student=student)
            mark.append(mark_.mark)
        context = {
            'student': students,
            'mark': mark,
        }
        return render(request, 'marks_by_group.html', context)
