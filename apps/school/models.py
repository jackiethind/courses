from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #   return self.course_name + " " + self.created_at

# class Description(models.Model):
#     course = models.OneToOneField(Course)
    # def __str__(self):
    #   return self.description

# Create your models here.
