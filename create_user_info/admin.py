from django.contrib import admin
from .models import course_names,course_explore ,contact_form ,enroll_form
# Register your models here.


class course_exploreAdmin(admin.ModelAdmin):
    class Meta:
        model=course_explore
        list_display=['course_name','descption']


class enrollAdmin(admin.ModelAdmin):
    class Meta:
        model=enroll_form
        list_display=['name','email','phonenumber','course']
        search_fields=('course')

admin.site.register(course_explore,course_exploreAdmin)
admin.site.register(course_names) 
admin.site.register(contact_form) 
admin.site.register(enroll_form,enrollAdmin) 

 