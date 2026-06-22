from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Department(models.Model):
    """Department model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    """Custom User model"""
    ROLE_CHOICES = [
        ('DEPARTMENT', 'Department User'),
        ('FINANCE', 'Finance User'),
        ('MANAGEMENT', 'Management'),
        ('ADMIN', 'System Admin'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='DEPARTMENT')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"

class Request(models.Model):
    """Main Request model"""
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('RECEIVED', 'Received by Finance'),
        ('PROCESSING', 'Processing'),
        ('APPROVED', 'Approved'),
        ('PAID', 'Paid'),
        ('CLEARED', 'Cleared'),
        ('RETURNED', 'Returned'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_number = models.CharField(max_length=50, unique=True)
    request_type = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    department_name = models.CharField(max_length=100)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    financial_year = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='SUBMITTED')
    return_reason = models.TextField(blank=True)
    submission_date = models.DateField(auto_now_add=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_reference = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.request_number} - {self.request_type}"
