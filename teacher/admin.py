from django.contrib import admin
from teacher.models import Teacher
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AdminTeacher(admin.ModelAdmin):
    list_display=['id','first_name','email_address','mobile_number','subject_taught']
admin.site.register(Teacher,AdminTeacher)





# @admin.register(Teacher)
# class AdminTeacher(ImportExportModelAdmin):
#     pass