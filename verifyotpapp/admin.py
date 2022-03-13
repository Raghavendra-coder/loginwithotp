from django.contrib import admin
from .models import *


class VerificationDetailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'email_is_verified')


class OTPAdmin(admin.ModelAdmin):
    list_display = ('email', 'attempts', 'otp')


# Register your models here.
admin.site.register(VerificationDetails, VerificationDetailsAdmin)
admin.site.register(OTP, OTPAdmin)
