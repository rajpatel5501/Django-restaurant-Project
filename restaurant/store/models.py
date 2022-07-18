from django.db import models
from account.models import User
import jwt
from django.contrib.auth import get_user_model
from restaurant.settings import SIMPLE_JWT
class Product(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=50)
    

    price = models.IntegerField(default=0)
    description = models.CharField(
        verbose_name='Description',
        max_length=255, default='')
    user= models.ForeignKey(User , on_delete=models.CASCADE  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    @staticmethod
    def get_owner_products(request):
        if 'ath' in request.session:
            auth = request.session['ath']
            token = auth['access']
            user = jwt.decode(token,options={"verify_signature": False})
            usertType = auth['userType']
            
            UserModel = get_user_model()
            usrId = user['user_id']
           
            userData = UserModel.objects.filter(
         id = usrId
            )
     
            products = Product.objects.filter(user = userData[0].id )
     
            return products
        else:
            None
    

    @staticmethod
    def get_all_products():
        products = Product.objects.all()
     
        return products
    
