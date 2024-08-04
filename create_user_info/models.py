from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class course_names(models.Model):
    course=models.CharField(max_length=50)

    def __str__(self):
        return self.course


class course_explore(models.Model):
    course_name = models.ForeignKey(course_names, on_delete=models.CASCADE)
    description = RichTextUploadingField(null=True, blank=True, default='Here is programming knowledge and enhance your skills')

    def __str__(self):
        return f"{self.course_name} "  # Optional: Return a string representation for course_explore

    
class student_common_info(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    class Meta:
        abstract=True

class contact_form(student_common_info):
    message=models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email} - {self.message}'
    
class enroll_form(student_common_info):
    phonenumber=models.IntegerField()
    course=models.ForeignKey(course_names,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phonenumber} - {self.course}'
    
