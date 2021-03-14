from rest_framework.generics import ListAPIView

from .serializers import DisciplineSerializer, GroupSerializer, StudentSerializer, MarkSerializer
from ..models import Discipline, Group, Student, Mark


class DisciplineListAPIView(ListAPIView):

    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()


class GroupListAPIView(ListAPIView):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class StudentListAPIView(ListAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class MarkListAPIView(ListAPIView):

    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
