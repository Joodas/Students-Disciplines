from rest_framework import serializers

from ..models import Discipline, Group, Student, Mark, Teacher


class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = '__all__'
        depth = 1


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects)

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class MarkSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects)
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects)

    class Meta:
        model = Mark
        fields = '__all__'
        depth = 1


class BaseStaffSerializer:
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


class TeacherSerializer(BaseStaffSerializer, serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1
