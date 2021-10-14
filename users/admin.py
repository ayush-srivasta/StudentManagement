from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.CustomBaseuser)
admin.site.register(models.Department)
admin.site.register(models.Year)
admin.site.register(models.TeacherProfile)
admin.site.register(models.StudentProfile)
admin.site.register(models.Marks)
admin.site.register(models.Subject)