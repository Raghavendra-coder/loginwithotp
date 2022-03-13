from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import OTP
from datetime import datetime, date
import datetime as dt

class GetOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('email',)

    def validate_email(self, value):
        print('11111111111111111111111222222222222222222')
        email = value
        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("this email has not been registered")

        otp_qry = OTP.objects.filter(email=email).first()
        # if otp_qry.failed:

        if otp_qry:
            saved_time_s = otp_qry.updated_at.second
            current_time_s = datetime.now().second
            saved_time_m = otp_qry.updated_at.minute
            current_time_m = datetime.now().minute
            saved_time_h = otp_qry.updated_at.hour
            current_time_h = datetime.now().hour
            current_time = f'{current_time_h}:{current_time_m}:{current_time_s}'
            saved_time = f'{saved_time_h}:{saved_time_m}:{saved_time_s}'
            FMT = '%H:%M:%S'
            time_diff = datetime.strptime(current_time, FMT) - datetime.strptime(saved_time, FMT)
            if time_diff.seconds < 60:
                raise serializers.ValidationError(f"Resend OTP will be enabled after {60-time_diff.seconds} seconds")
            otp_qry.updated_at = datetime.now()
            otp_qry.save()
        return email


class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('email', 'otp')

    def validate(self, attrs):
        email = attrs['email']
        otp = attrs['otp']
        otp_qry = OTP.objects.filter(email=email).first()
        user = User.objects.filter(email=email).first()
        saved_time_s = otp_qry.updated_at.second
        current_time_s = datetime.now().second
        saved_time_m = otp_qry.updated_at.minute
        current_time_m = datetime.now().minute
        saved_time_h = otp_qry.updated_at.hour
        current_time_h = datetime.now().hour
        current_time = f'{current_time_h}:{current_time_m}:{current_time_s}'
        saved_time = f'{saved_time_h}:{saved_time_m}:{saved_time_s}'
        FMT = '%H:%M:%S'
        time_diff = datetime.strptime(current_time, FMT) - datetime.strptime(saved_time, FMT)
        if not user:
            raise serializers.ValidationError("this email has not been registered")
        if not email:
            raise serializers.ValidationError("Please generate OTP first")
        if otp_qry.attempts >= 5:
            otp_qry.failed = True
            otp_qry.save()
            raise serializers.ValidationError(f"Maximum 5 attempts allowed.Try after Sometime")
        if time_diff.seconds >= 3600 and otp_qry.attempts >= 5:
            otp_qry.failed = False
            otp_qry.attempts = 0
            otp_qry.updated_at = datetime.now()
            otp_qry.save()


        if str(otp) != str(otp_qry.otp):
            otp_qry.attempts += 1
            otp_qry.save()
            raise serializers.ValidationError("invalid OTP.")
        return attrs
