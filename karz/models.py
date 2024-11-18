from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=15, null=False)
    address = models.TextField(null=False)
    def __str__(self):
        return self.username


class Limit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    limit_amount = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - limit: {self.limit_amount.__str__()}"

STATUS_TYPES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_TYPES, default='pending')
    def __str__(self):
        return f"{self.user.username} - amount: {self.loan_amount.__str__()} - due date: {self.due_date.__str__()}"

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    payment_amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.loan} - amount: {self.payment_amount.__str__()} - payment date: {self.payment_date.__str__()}"


@receiver(post_save, sender=Loan)
def update_limit_on_loan(sender, instance, created, **kwargs):
    if created:
        limit = Limit.objects.get(user=instance.user)
        limit.limit_amount -= instance.loan_amount
        limit.save()

@receiver(post_save, sender=Payment)
def update_limit_on_payment(sender, instance, created, **kwargs):
    if created:
        limit = Limit.objects.get(user=instance.loan.user)
        limit.limit_amount += instance.payment_amount
        limit.save()


@receiver(post_save, sender=Payment)
def update_loan_amount_on_payment(sender, instance, created, **kwargs):
    if created:
        loan = Loan.objects.get(id=instance.loan.id)
        loan.loan_amount -= instance.payment_amount
        loan.save()

@receiver(post_save, sender=Payment)
def update_status_on_payment(sender, instance, created, **kwargs):
    if created:
        loan = Loan.objects.get(id=instance.loan.id)
        if loan.loan_amount == 0:
            loan.status = 'completed'
            loan.save()
