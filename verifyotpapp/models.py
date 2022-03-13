from django.db import models

# Create your models here.
class VerificationDetails(models.Model):
     email = models.CharField(max_length=30, unique=True)
     otp = models.IntegerField(null=True)
     recieved_time = models.DateTimeField(auto_now_add=True)
     update = models.DateTimeField(auto_now=True)
     attempts = models.IntegerField(default=0)
     otp_expire_time = models.DateTimeField()
     email_is_verified = models.BooleanField(default=False)

     def __str__(self):
         return self.email


class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    attempts = models.IntegerField(default=0)
    created_at_date = models.DateTimeField(auto_now_add=True)
    failed = models.BooleanField(default=False)