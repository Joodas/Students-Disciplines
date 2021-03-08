from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg

from .models import Mark, Discipline, Group, Student


class BaseView(View):
    disciplines = Discipline.objects.all()
    groups = Group.objects.all()

    def get(self, request):
        context = {
            'disciplines': self.disciplines,
            'groups': self.groups,
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
    mark = []
    disciplines = []
    mark_avg = []

    def get(self, request, **kwargs):
        group_slug = kwargs.get('slug')
        group = Group.objects.get(slug=group_slug)
        students = Student.objects.filter(group=group)

        for student in students:
            mark_ = Mark.objects.all().filter(student=student)
            mark_avg_ = mark_.aggregate(average_mark=Avg('mark'))
            self.mark.append(mark_)
            self.mark_avg.append(mark_avg_)
            self.disciplines.append(mark_)
        context = {
            'student': students,
            'mark': self.mark,
            'disciplines': list(set(self.disciplines)),
            'mark_avg': self.mark_avg,
        }
        return render(request, 'marks_by_group.html', context)
