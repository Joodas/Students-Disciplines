import factory
from . import models


class TeacherFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Teacher

    first_name = "Ivan"
    last_name = "Ivanov"
