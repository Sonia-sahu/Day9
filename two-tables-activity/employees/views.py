from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

from django.urls import reverse_lazy 

from .models import Employee 

 

class EmployeeListView(ListView): 

    model = Employee 

    context_object_name = 'employees' 

    template_name = 'employees/employee_list.html' 

 

class EmployeeDetailView(DetailView): 

    model = Employee 

    context_object_name = 'employee' 

    template_name = 'employees/employee_detail.html' 

 

class EmployeeCreateView(CreateView): 

    model = Employee 

    fields = ['name', 'designation', 'department'] 

    template_name = 'employees/employee_form.html' 

    success_url = reverse_lazy('employee-list') 

 

class EmployeeUpdateView(UpdateView): 

    model = Employee 

    fields = ['name', 'designation', 'department'] 

    template_name = 'employees/employee_form.html' 

    success_url = reverse_lazy('employee-list') 

 

class EmployeeDeleteView(DeleteView): 

    model = Employee 

    context_object_name = 'employee' 

    template_name = 'employees/employee_confirm_delete.html' 

    success_url = reverse_lazy('employee-list') 