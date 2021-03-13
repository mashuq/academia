from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from faker import Faker
import re


class Command(BaseCommand):
    help = 'Modify Username and Password'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address of the person to modify')

    def handle(self, *args, **kwargs):
        fake = Faker()
        email = kwargs['email']
        user = User.objects.get(email=email)
        username = re.sub(r'\W+', '', email.split("@")[0])
        user.username = username
        random_password =  fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
        password = make_password(random_password)
        user.password = password
        user.save()
        print('email : ' + email)
        print('নুরুল কুরআন একাডেমিতে স্বাগতম')
        print()
        print('নুরুল কুরআন একাডেমিতে শিক্ষার্থী হিসেবে লগইন করুন: http://school.nlquran.com/#/Student')
        print('আপনার ইউজারনেম : ' + user.username)
        print('আপনার পাসওয়ার্ড : ' + random_password)