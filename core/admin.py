# Register your models here.
from django.contrib import admin
from .models import Customer, Worker, Estimate, Project, Invoice

admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(Estimate)
admin.site.register(Project)
admin.site.register(Invoice)
