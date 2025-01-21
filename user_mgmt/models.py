from django.db import models
import datetime

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    user_type = models.ForeignKey('UserTypes', on_delete=models.CASCADE)  
    fullname = models.CharField(max_length=30)
    qualification = models.CharField(max_length=20)
    current_year = datetime.datetime.now().year
    passing_year = models.IntegerField(
        choices=[(year, year) for year in range(1900, current_year + 5)],
        default=current_year,
        verbose_name="Year of Passing Out"
    )
    address = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.username

class UserTypes(models.Model):  
    user_type_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class SystemModules(models.Model):  
    system_module_id = models.AutoField(primary_key=True)
    system_module_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    module_url = models.CharField(max_length=100)

    def __str__(self):
        return self.system_module_name

class UserTypeModuleMapping(models.Model):
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE)
    system_module = models.ForeignKey(SystemModules, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_type.user_type} - {self.system_module.system_module_name}"
