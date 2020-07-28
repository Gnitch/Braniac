from django.contrib import admin

from .models import Quiz, Question, Options, StudentQuizInfo, Class, Job, Comments

admin.site.register(Quiz)
admin.site.register(Class)
admin.site.register(Job)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(StudentQuizInfo)
admin.site.register(Comments)

