from django.urls import path
from account.views import  UserLoginView, UserRegistrationView, UserLogoutView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    

]