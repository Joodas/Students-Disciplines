from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, viewsets

from .serializers import (
    DisciplineSerializer,
    GroupSerializer,
    StudentSerializer,
    MarkSerializer,
    TeacherSerializer,
)
from ..models import Discipline, Group, Student, Mark, Teacher


# TODO: причесать api
# кэширование
# hypermedia ссылки


class MarkPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 200


class Permission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_superuser
        else:
            return False


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [Permission, ]


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    pagination_class = MarkPagination
    queryset = Mark.objects.all()
    lookup_field = 'id'
    filter_backends = [SearchFilter]
    search_fields = ['student', 'discipline']
    permission_classes = [Permission, ]


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [SearchFilter]
    lookup_field = 'id'
    search_fields = ['group']
    permission_classes = [Permission, ]


class DisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
    permission_classes = [Permission, ]


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [Permission, ]
