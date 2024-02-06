from django.db import models 

class Employee(models.Model):  
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=15)  
    
class Team(models.Model):    
    team_name = models.CharField(max_length=255) 
    
class EmployeeProfile(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    status = models.CharField(max_length=255) 
    salary = models.DecimalField(max_digits=10, decimal_places=2) 
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True) 
