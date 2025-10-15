# Create your tests here.
from django.test import TestCase
from .models import Customer, Estimate

class EstimateModelTest(TestCase):
    def test_create_estimate_and_defaults(self):
        cust = Customer.objects.create(name="Test Customer")
        est = Estimate.objects.create(customer=cust, outline="Short outline", amount=1000)
        self.assertEqual(est.status, "pending")
        self.assertEqual(est.customer.name, "Test Customer")
