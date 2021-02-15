import factory
from factory.django import DjangoModelFactory
from .models import *
import factory.fuzzy


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
