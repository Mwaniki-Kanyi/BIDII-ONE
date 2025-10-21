from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from core.models import Project, Invoice

class Command(BaseCommand):
    help = "Send reminders for upcoming projects and due invoices"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        # Project start reminders (2 days before start)
        upcoming_projects = Project.objects.filter(start_date=today + timedelta(days=2))
        for p in upcoming_projects:
            send_mail(
                subject="Upcoming Project Start Reminder",
                message=f"Hello {p.estimate.customer.name}, your project '{p.estimate.outline}' starts on {p.start_date}.",
                from_email=None,
                recipient_list=[p.estimate.customer.email],
                fail_silently=True,
            )

        # Invoice payment reminders (5 days before due)
        upcoming_invoices = Invoice.objects.filter(paid=False, due_date=today + timedelta(days=5))
        for i in upcoming_invoices:
            send_mail(
                subject="Invoice Payment Reminder",
                message=f"Dear {i.project.estimate.customer.name}, your payment for '{i.project.estimate.outline}' is due on {i.due_date}.",
                from_email=None,
                recipient_list=[i.project.estimate.customer.email],
                fail_silently=True,
            )

        self.stdout.write(self.style.SUCCESS("Reminders sent successfully."))
