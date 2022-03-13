import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import GetOTPSerializer, VerifyOTPSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import random
from rest_framework_jwt.settings import api_settings
import smtplib
from ..models import *

# Create your views here.




class GetOTPView(APIView):
    # authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer = GetOTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = random.randint(0, 9999)
            if otp < 1000:
                otp = f'{otp:04}'
            updated_at = datetime.datetime.now().date()
            otp_qry = OTP.objects.filter(email=serializer.validated_data['email'])
            otp_qry.delete()
            serializer.save(otp=otp, updated_at=updated_at)
            response = {'status': True, 'otp': otp}

            #sending mail
            sender = "rkeshari50@gmail.com"
            password = "jubwshrhprxaeajf"
            reciever = serializer.data['email']
            message = f"Thanks for logging in.Use {otp} as your otp"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            print('login Successful')
            server.sendmail(sender, reciever, message)
            print("MAil sent")



        else:
            print(serializer.errors)
            response = serializer.errors

        return Response(response)


class VerifyOTPView(APIView):

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            email = serializer.data['email']
            user = User.objects.filter(email=email).first()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = {'status': True,'token': token}

            #sending mail

            sender = "rkeshari50@gmail.com"
            password = "jubwshrhprxaeajf"
            reciever = serializer.data['email']
            # reciever = "raghavendra.1822cs1103@kiet.edu"
            msg = f"Email Verify.Your token is : {token}"
            print(msg)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            print('login Successful')
            server.sendmail(sender, reciever, f"OTP verified. Your token is - {token}")


        else:
            response = serializer.errors

        return Response(response)
