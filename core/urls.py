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

]
