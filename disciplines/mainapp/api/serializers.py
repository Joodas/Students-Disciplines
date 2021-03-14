from rest_framework import serializers

from ..models import Discipline, Group, Student, Mark


class DisciplineSerializer(serializers.ModelSerializer):

    discipline_name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Discipline
        fields = [
            'id', 'discipline_name', 'slug',
        ]


class GroupSerializer(serializers.ModelSerializer):

    group_name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Group
        fields = [
            'id', 'group_name', 'slug',
        ]


class StudentSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Student
        fields = [
            'id', 'group', 'first_name', 'last_name',
        ]


class MarkSerializer(serializers.ModelSerializer):

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects)
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects)
    mark = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Mark
        fields = [
            'id', 'student', 'discipline', 'mark',
        ]
