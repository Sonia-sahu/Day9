from django.urls import path 

from .views import DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView 

 

urlpatterns = [ 

    path('', DepartmentListView.as_view(), name='department-list'), 

    path('new/', DepartmentCreateView.as_view(), name='department-new'), 

    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'), 

    path('<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department-edit'), 

    path('<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'), 

] 