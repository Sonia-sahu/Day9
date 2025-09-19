from django.db import models 

from django.urls import reverse 

from departments.models import Department 

 

class Employee(models.Model): 

    empid = models.AutoField(primary_key=True) 

    name = models.CharField(max_length=100) 

    designation = models.CharField(max_length=100) 

    department = models.ForeignKey(Department, on_delete=models.CASCADE) 

 

    def __str__(self): 

        return self.name 

 

    def get_absolute_url(self): 

        return reverse('employee_detail', args=[str(self.empid)]) 