import random

from django.db import transaction
from django.core.management.base import BaseCommand

from core.models import *
from core.factories import *

from django.contrib.contenttypes.models import ContentType

NUM_CATEGORIES = 105
NUM_COURSES = 107
NUM_SECTIONS = 532
NUM_SESSION = 1500
NUM_QUESTIONS = 100


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # ct_mcq = ContentType.objects.get_for_model(MultipleChoiceQuestion)
        # MultipleChoiceQuestion.objects.filter(
        #     polymorphic_ctype__isnull=True).update(polymorphic_ctype=ct_mcq)

        # ct_sq = ContentType.objects.get_for_model(ShortQuestion)
        # ShortQuestion.objects.filter(
        #     polymorphic_ctype__isnull=True).update(polymorphic_ctype=ct_sq)

        # ct_bq = ContentType.objects.get_for_model(BroadQuestion)
        # BroadQuestion.objects.filter(
        #     polymorphic_ctype__isnull=True).update(polymorphic_ctype=ct_bq)

        # self.stdout.write("Deleting old data...")
        # models = [BroadQuestion, ShortQuestion, MultipleChoiceQuestion]
        # for m in models:
        #     m.objects.all().delete()

        # self.stdout.write("Creating new data...")
        # course_categories = []
        # for _ in range(NUM_CATEGORIES):
        #     course_category = CourseCategoryFactory()
        #     course_categories.append(course_category)

        # courses = []
        # for _ in range(NUM_COURSES):
        #     course_cat = random.choice(
        #         course_categories
        #     )
        #     course = CourseFactory(course_category=course_cat)
        #     courses.append(course)

        # sections = []
        # for _ in range(NUM_SECTIONS):
        #     course = random.choice(
        #         courses
        #     )
        #     section = SectionFactory(course=course)
        #     sections.append(section)

        # sessions = []
        # for _ in range(NUM_SECTIONS):
        #     course = random.choice(
        #         courses
        #     )
        #     session = SessionFactory(course=course)
        #     sessions.append(session)

        mcqs = []
        for _ in range(NUM_QUESTIONS):
            # session = random.choice(
            #     sessions
            # )
            session = Session.objects.order_by("?").first()
            mcq = McqFactory(session=session)
            mcqs.append(mcq)

        sqs = []
        for _ in range(NUM_QUESTIONS):
            # session = random.choice(
            #     sessions
            # )
            session = Session.objects.order_by("?").first()
            sq = SqFactory(session=session)
            sqs.append(sq)

        bqs = []
        for _ in range(NUM_QUESTIONS):
            # session = random.choice(
            #     sessions
            # )
            session = Session.objects.order_by("?").first()
            bq = BqFactory(session=session)
            bqs.append(bq)
