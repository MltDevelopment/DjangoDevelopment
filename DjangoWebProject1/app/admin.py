from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.ClassGrade)
admin.site.register(models.AllClassGrade)
admin.site.register(models.AllTest)
