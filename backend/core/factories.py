import factory
from factory.django import DjangoModelFactory
from .models import *
import factory.fuzzy
from django.utils import timezone
import random


class CourseCategoryFactory(DjangoModelFactory):
    class Meta:
        model = CourseCategory
    name = factory.Faker("bs")


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker("bs")
    code = factory.fuzzy.FuzzyText(length=10)
    description = factory.Faker("paragraph")
    curriculum = factory.Faker("paragraph")
    image = 'https://picsum.photos/400/250'
    visible = factory.Faker("boolean")


class SectionFactory(DjangoModelFactory):
    class Meta:
        model = Section

    name = factory.Faker("bs")
    start_date = factory.Faker(
        "date_time", tzinfo=timezone.get_current_timezone())
    end_date = factory.Faker(
        "date_time", tzinfo=timezone.get_current_timezone())
    visible = factory.Faker("boolean")


class SessionFactory(DjangoModelFactory):
    class Meta:
        model = Session

    name = factory.Faker("bs")
    serial = factory.Faker("random_int")


class McqFactory(DjangoModelFactory):
    class Meta:
        model = MultipleChoiceQuestion

    question = factory.Faker("sentence")
    choice1 = factory.Faker("words")
    choice2 = factory.Faker("words")
    choice3 = factory.Faker("words")
    choice4 = factory.Faker("words")
    correct_choice = random.choice([choice1, choice2, choice3, choice4])
    mark = 1


class SqFactory(DjangoModelFactory):
    class Meta:
        model = ShortQuestion

    question = factory.Faker("sentence")
    mark = 5


class BqFactory(DjangoModelFactory):
    class Meta:
        model = BroadQuestion

    question = factory.Faker("sentence")
    mark = 10
