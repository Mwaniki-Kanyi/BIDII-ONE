# Create your models here.
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self): return f"{self.name}"

class Worker(models.Model):
    ROLE_CHOICES = [("bricklayer","Bricklayer"),("carpenter","Carpenter"),("plumber","Plumber")]
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self): return f"{self.name} ({self.role})"

class Estimate(models.Model):
    STATUS = [("pending","Pending"),("approved","Approved"),("rejected","Rejected")]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="estimates")
    outline = models.TextField()
    detailed_description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    visit_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="pending")

    def __str__(self): return f"Estimate #{self.id} - {self.customer.name}"

class Project(models.Model):
    estimate = models.OneToOneField(Estimate, on_delete=models.CASCADE, related_name="project")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    workers = models.ManyToManyField(Worker, blank=True)
    materials_ordered = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self): return f"Project #{self.id} for {self.estimate.customer.name}"

class Invoice(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="invoice")
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): return f"Invoice #{self.id} - {self.project.estimate.customer.name}"
