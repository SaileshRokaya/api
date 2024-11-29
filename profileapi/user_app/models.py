from django.db import models

# Create your models here.

class UserDetail(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    EDUCATION_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    # photo = models.ImageField(upload_to='photos/')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    skills = models.JSONField()  # A list of skills
    education = models.CharField(max_length=2, choices=EDUCATION_CHOICES)

    def __str__(self):
        return self.full_name
