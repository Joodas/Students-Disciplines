from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import (
    DisciplineSerializer,
    GroupSerializer,
    StudentSerializer,
    MarkSerializer,
    TeacherSerializer,
    PostgraduateSerializer,
)
from ..models import Discipline, Group, Student, Mark, Teacher, Postgraduate


class DisciplineListAPIView(ListAPIView):

    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()


class GroupListAPIView(ListAPIView):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class StudentListAPIView(ListAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['group']


class StudentRetrieveAPIView(RetrieveAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'


class MarkPagination(PageNumberPagination):

    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 200


class MarkAPIView(ListCreateAPIView, RetrieveUpdateAPIView):

    serializer_class = MarkSerializer
    pagination_class = MarkPagination
    queryset = Mark.objects.all()
    lookup_field = 'id'
    filter_backends = [SearchFilter]
    search_fields = ['student', 'discipline']


class TeacherListAPIView(ListAPIView):

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class PostgraduateListAPIView(ListAPIView):

    serializer_class = PostgraduateSerializer
    queryset = Postgraduate.objects.all()
