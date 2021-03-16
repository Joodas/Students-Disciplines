from django.test import TestCase

from .algorithms import Arithmetic, Median
from .factory import FactoryManager
from .models import Teacher, Postgraduate


class DisciplinesTestCases(TestCase):

    def setUp(self) -> None:
        self.array = [1, 2, 3, 4, 5, 6, 7, 8]
        self.arithmetic = Arithmetic()
        self.median = Median()
        self.teacher_factory = FactoryManager()
        self.postgraduate_factory = FactoryManager()

    def test_arithmetic(self):
        self.assertEqual(self.arithmetic.calculate_avg(self.array), 4.5)

    def test_median(self):
        self.assertEqual(self.median.calculate_avg(self.array), 4.5)

    def test_teacher_factory(self):
        new_teacher = self.teacher_factory.concrete_factory(
            'Teacher',
            first_name='Ivan',
            last_name='Petrov'
        )
        self.assertIn(new_teacher, Teacher.objects.all())

    def test_postgraduate_factory(self):
        new_postgraduate = self.postgraduate_factory.concrete_factory(
            'Postgraduate',
            first_name='Semen',
            last_name='Lomov'
        )
        self.assertIn(new_postgraduate, Postgraduate.objects.all())
