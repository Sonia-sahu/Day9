from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

from django.urls import reverse_lazy 

from .models import Department 

 

class DepartmentListView(ListView): 

    model = Department 

    context_object_name = 'departments' 

    template_name = 'departments/department_list.html' 

 

class DepartmentDetailView(DetailView): 

    model = Department 

    context_object_name = 'department' 

    template_name = 'departments/department_detail.html' 

 

class DepartmentCreateView(CreateView): 

    model = Department 

    fields = ['deptname', 'hod', 'location'] 

    template_name = 'departments/department_form.html' 

    success_url = reverse_lazy('department-list') 

 

class DepartmentUpdateView(UpdateView): 

    model = Department 

    fields = ['deptname', 'hod', 'location'] 

    template_name = 'departments/department_form.html' 

    success_url = reverse_lazy('department-list') 

 

class DepartmentDeleteView(DeleteView): 

    model = Department 

    context_object_name = 'department' 

    template_name = 'departments/department_confirm_delete.html' 

    success_url = reverse_lazy('department-list') 