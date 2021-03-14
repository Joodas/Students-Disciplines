from itertools import zip_longest

from django.shortcuts import render
from django.views.generic import View

from .models import Mark, Discipline, Group, Student
from .algorythms import *


class BaseView(View):
    @staticmethod
    def get(request):
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
        avg_mark_ = marks.values_list('mark', flat=True)
        avg_mark = Query.get_query(avg_mark_, 'Arithmetic')
        context = {
            'discipline': discipline,
            'marks': marks,
            'avg_marks': avg_mark,
        }
        return render(request, 'discipline_marks.html', context)


class MarksManagerByGroup(View):
    @staticmethod
    def get(request, **kwargs):
        group_slug = kwargs.get('slug')
        group = Group.objects.get(slug=group_slug)
        students = Student.objects.filter(group=group)
        disciplines = []
        mark = []
        for student in students:
            mark_avg = []
            mark_ = Mark.objects.filter(student=student)
            mark += mark_.values_list('mark', flat=True)
            disciplines += mark_
            mark_avg.append(Query.get_query(mark, 'Median'))
        context = {
            'group': group,
            'student': students,
            'disciplines': disciplines,
            'mark': mark,
            'mark_avg': mark_avg,
        }
        print(context)
        return render(request, 'marks_by_group.html', context)
