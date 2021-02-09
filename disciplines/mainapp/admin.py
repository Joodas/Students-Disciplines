from django.contrib import admin

from .models import *

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Discipline)
admin.site.register(Mark)
admin.site.register(StudentList)
