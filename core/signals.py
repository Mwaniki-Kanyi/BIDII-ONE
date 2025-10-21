from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import Estimate, Project, Invoice

# Auto-create Project when Estimate is approved
@receiver(post_save, sender=Estimate)
def create_project_from_estimate(sender, instance, created, **kwargs):
    if not created and instance.status == 'approved':
        # check if project already exists
        if not hasattr(instance, 'project'):
            Project.objects.create(
                estimate=instance,
                start_date=timezone.now().date() + timedelta(days=7),  # default start in 7 days
            )
            send_mail(
                subject="Estimate Approved - Project Scheduled",
                message=f"Your estimate has been approved! Work will begin around {timezone.now().date() + timedelta(days=7)}.",
                from_email=None,
                recipient_list=[instance.customer.email],
                fail_silently=True,
            )

# Auto-generate Invoice when Project is marked completed
@receiver(pre_save, sender=Project)
def create_invoice_when_completed(sender, instance, **kwargs):
    if instance.pk:  # existing record
        old = Project.objects.get(pk=instance.pk)
        # if completed changed from False → True
        if not old.completed and instance.completed:
            # ensure invoice doesn't already exist
            if not hasattr(instance, 'invoice'):
                due_date = timezone.now().date() + timedelta(days=30)
                Invoice.objects.create(
                    project=instance,
                    total_cost=instance.estimate.amount,
                    due_date=due_date,
                )
                send_mail(
                    subject="Invoice Generated - Bidii Quality Builders",
                    message=f"Your invoice for project '{instance.estimate.outline}' has been created. Please make payment by {due_date}.",
                    from_email=None,
                    recipient_list=[instance.estimate.customer.email],
                    fail_silently=True,
                )
