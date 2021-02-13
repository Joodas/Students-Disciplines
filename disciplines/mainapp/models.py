from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name='Группа')
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return self.group_name


class Student(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=255, verbose_name='Название дисциплины')
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return self.discipline_name


class Mark(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name='Предмет', on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {} {}'.format(self.student, self.discipline, self.mark)


class StudentList(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return 'Список группы {}'.format(self.group)