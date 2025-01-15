from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=50, unique=True) 
    course_name = models.CharField(max_length=200)  
    description = models.TextField()  
    course_duration = models.IntegerField()  #in months
    course_fees = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.course_name