from django.urls import path
from .views import *

urlpatterns = [
    path('api/getotp/', GetOTPView.as_view()),
    path('api/verifyotp/',VerifyOTPView.as_view()),
]