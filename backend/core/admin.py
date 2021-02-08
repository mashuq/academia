from django.contrib import admin

from . import models

registered_models = [
    models.Testimonial, 
    models.Teacher,
    models.Course,
    models.CourseCategory,
]

admin.site.register(registered_models)

