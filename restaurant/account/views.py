from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import jwt
from django.shortcuts import render
from restaurant.settings import SIMPLE_JWT
User = get_user_model()

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'userType': user.userType
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):

    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    request.session['ath'] = token
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    # if 'ath' in request.session:
    #     auth = request.session['ath']
    #     token = auth['access']
    #     user = jwt.decode(token,options={"verify_signature": False})
    #     usertType = auth['userType']
    #     # print(usertType)
    #     # return redirect( 'index' )
    # else:
    #   return redirect('login' )
    

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):

  
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')

    password = serializer.data.get('password')
    print(email , password)

    user = authenticate(email = email, password=password)

    # userType=request.POST['userType']
    if user is not None:
      token = get_tokens_for_user(user)
      request.session['ath'] = token
      
      # request.session['typ'] = userType
      # print(user.userType)
    # This redirecting is for just using the data in template. If you want to use it as
    # a api you need to remove this line and uncomment the next line.
      redirect('index')
    
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    # else:
    # This redirecting is for just using the data in template. If you want to use it as
    # a api you need to remove this line and uncomment the next line.
      # return redirect('login')
      # return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserLogoutView(APIView):
  renderer_classes = [UserRenderer]
  def post(self , request , format=None):
     del request.session['ath']
     return Response({ 'msg':'Logout Success'}, status=status.HTTP_200_OK)