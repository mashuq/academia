from core.models import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "enrolls users to section"

    def handle(self, *args, **kwargs):
        section_id = 5
        students = Student.objects.all()
        for student in students:
            try:
                enrolment = Enrolment(student=student, section_id=section_id, final_grade=0)
                enrolment.save() 
                print('saved' + enrolment.__str__())
            except Exception as e:
                print(e)
