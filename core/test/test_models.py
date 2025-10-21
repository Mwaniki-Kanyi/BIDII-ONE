from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from core.models import Customer, Worker, Estimate, Project, Invoice

class ModelCreationTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com")
        self.worker = Worker.objects.create(name="James", role="carpenter")
        self.estimate = Estimate.objects.create(
            customer=self.customer,
            outline="Build kitchen cabinets",
            detailed_description="Custom wooden cabinets for kitchen renovation.",
            amount=50000,
            status="approved"
        )

    def test_customer_created(self):
        self.assertEqual(self.customer.name, "John Doe")

    def test_estimate_defaults(self):
        self.assertEqual(self.estimate.status, "approved")

    def test_project_creation_manual(self):
        project = Project.objects.create(
            estimate=self.estimate,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=10)
        )
        project.workers.add(self.worker)
        self.assertEqual(project.estimate.outline, "Build kitchen cabinets")
        self.assertIn(self.worker, project.workers.all())

    def test_invoice_generation_manual(self):
        project = Project.objects.create(
            estimate=self.estimate,
            completed=True,
            end_date=timezone.now().date(),
        )
        invoice = Invoice.objects.create(
            project=project,
            total_cost=self.estimate.amount,
            due_date=timezone.now().date() + timedelta(days=30)
        )
        self.assertEqual(invoice.project.estimate.customer.name, "John Doe")
        self.assertFalse(invoice.paid)
