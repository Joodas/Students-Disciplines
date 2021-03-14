import factory
from . import models


class TeacherFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Teacher

    first_name = ""
    last_name = ""


class PostgraduateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Postgraduate

    first_name = ""
    last_name = ""


class Fabric:

    def concrete_factory(self,
                         factory_type,
                         first_name='',
                         last_name=''):
        raise NotImplementedError


class FactoryManager(Fabric):

    def concrete_factory(self,
                         factory_type,
                         first_name='',
                         last_name=''):
        if factory_type == 'Teacher':
            return TeacherFactory(first_name=first_name, last_name=last_name)
        elif factory_type == 'Postgraduate':
            return PostgraduateFactory(first_name=first_name, last_name=last_name)
