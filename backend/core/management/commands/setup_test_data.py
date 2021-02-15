import random

from django.db import transaction
from django.core.management.base import BaseCommand

from core.models import *
from core.factories import *

NUM_CATEGORIES = 105
NUM_COURSES = 107


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Course, CourseCategory]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        course_categories = []
        for _ in range(NUM_CATEGORIES):
            course_category = CourseCategoryFactory()
            course_categories.append(course_category)

        courses = []
        for _ in range(NUM_COURSES):
            course_cat = random.choice(
                course_categories
            )
            course = CourseFactory(course_category=course_cat)
            courses.append(course)
