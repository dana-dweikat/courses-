from django.contrib import admin
from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Courses,CoursesAdmin )
