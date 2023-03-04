from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Company(models.Model):
    name = models.CharField(
        max_length=100, 
        help_text='company name'
    )
    established_date = models.DateField(auto_now=True)
    industry = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(
        max_length=100, 
        verbose_name='email address', 
        unique=True
    )

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    email = models.EmailField(
        max_length=100, 
        verbose_name='email address', 
        unique=True
    )
    

    def __str__(self):
        return self.user.email
