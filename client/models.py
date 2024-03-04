from django.db import models 
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):  
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=15)  
    EMPLOYEE_TYPE_CHOICES = [
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
    ]
    employee_type = models.CharField(max_length=9, choices=EMPLOYEE_TYPE_CHOICES, default='Employee')
    
class Team(models.Model):    
    team_name = models.CharField(max_length=255) 
    
class EmployeeProfile(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    status = models.CharField(max_length=255) 
    salary = models.DecimalField(max_digits=10, decimal_places=2) 
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True) 
