from django.db import models
import datetime


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20, choices=[('student', 'Student'), ('admin', 'Admin'), ('super admin', 'Super Admin')])
    fullname = models.CharField(max_length=30)
    qualification = models.CharField(max_length=20)
    current_year = datetime.datetime.now().year
    passing_year = models.IntegerField(
        choices=[(year, year) for year in range(1900, current_year + 5)],
        default=current_year,
        verbose_name="Year of Passing Out"
    )
    address = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)  # Added field
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.username
