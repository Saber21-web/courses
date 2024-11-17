from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(User, related_name="enrolled_courses")
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='usd')
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create(amount, status):
        return Payment.objects.create(amount=amount, status=status)
    
    def save(self, *args, **kwargs):
        # Custom save logic
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for - {self.amount} USD"