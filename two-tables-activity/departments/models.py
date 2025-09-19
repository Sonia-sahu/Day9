from django.db import models 

from django.urls import reverse 

 

class Department(models.Model): 

    id = models.AutoField(primary_key=True) 

    deptname = models.CharField(max_length=100) 

    hod = models.CharField(max_length=100) 

    location = models.CharField(max_length=100) 

 

    def __str__(self): 

        return self.deptname 

 

    def get_absolute_url(self): 

        return reverse('department_detail', args=[str(self.id)]) 