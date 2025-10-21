from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard.png", views.dashboard_plot, name="dashboard_plot"),
    # Customer CRUD routes
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),
    # Worker CRUD routes
    path('workers/', views.WorkerListView.as_view(), name='worker_list'),
    path('workers/add/', views.WorkerCreateView.as_view(), name='worker_add'),
    path('workers/<int:pk>/edit/', views.WorkerUpdateView.as_view(), name='worker_edit'),
    path('workers/<int:pk>/delete/', views.WorkerDeleteView.as_view(), name='worker_delete'),
    # Estimate CRUD routes
    path('estimates/', views.EstimateListView.as_view(), name='estimate_list'),
    path('estimates/add/', views.EstimateCreateView.as_view(), name='estimate_add'),
    path('estimates/<int:pk>/edit/', views.EstimateUpdateView.as_view(), name='estimate_edit'),
    path('estimates/<int:pk>/delete/', views.EstimateDeleteView.as_view(), name='estimate_delete'),
    # Project CRUD routes
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    # Invoice CRUD routes
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/add/', views.InvoiceCreateView.as_view(), name='invoice_add'),
    path('invoices/<int:pk>/edit/', views.InvoiceUpdateView.as_view(), name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),


]
