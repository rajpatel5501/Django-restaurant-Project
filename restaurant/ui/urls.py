from django.urls import path
from django.contrib.auth import views as auth_views
# from ui.views import LoginView
from . import views
from ui.views import AddProductView
urlpatterns = [
    path('',views.index , name='index'),
    path('owner',views.owner , name='owner'),
    path('login',views.login , name='login'),
    path('register',views.register , name='register'),
    path('addproduct',views.addproduct , name='addproduct'),
    path('owner/addproduct',AddProductView.as_view() , name='owneraddproduct'),

    

]