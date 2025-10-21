from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from core.models import Customer, Estimate, Project, Invoice

class AutomationSignalTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Jane Doe", email="jane@example.com")
        self.estimate = Estimate.objects.create(
            customer=self.customer,
            outline="Build a perimeter wall",
            detailed_description="A 50-meter stone perimeter wall.",
            amount=100000,
            status="pending"
        )

    def test_project_auto_created_on_estimate_approval(self):
        # Initially no project
        self.assertFalse(hasattr(self.estimate, 'project'))

        # Approve the estimate → should trigger project creation
        self.estimate.status = "approved"
        self.estimate.save()

        self.assertTrue(hasattr(self.estimate, 'project'))
        self.assertIsInstance(self.estimate.project, Project)

    def test_invoice_auto_created_on_project_completion(self):
        self.estimate.status = "approved"
        self.estimate.save()
        project = self.estimate.project

        # Initially no invoice
        self.assertFalse(hasattr(project, 'invoice'))

        # Complete project → should auto-generate invoice
        project.completed = True
        project.save()

        self.assertTrue(hasattr(project, 'invoice'))
        self.assertIsInstance(project.invoice, Invoice)
