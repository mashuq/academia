from django.contrib import admin

from . import models

registered_models = [
    models.Testimonial, 
    models.Teacher,
    models.Course,
    models.CourseCategory,
    models.Session,
    models.AudioLesson,
    models.VideoLesson,
    models.NoteLesson
]

admin.site.register(registered_models)

