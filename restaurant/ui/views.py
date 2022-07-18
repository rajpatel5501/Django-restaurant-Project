import jwt
from restaurant.settings import SIMPLE_JWT
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from store.models import Product
from ui.serializers import ProductAddSerializer
from rest_framework.views import APIView


def index(request):
    #   products = Product.get_owner_products(request)
    # products = Product.get_all_products()
    # context = {'products': products}

    if 'ath' in request.session:
        auth = request.session['ath']
        token = auth['access']
        user = jwt.decode(token, options={"verify_signature": False})
        usertType = auth['userType']

        
            # print(usertType)
        print(usertType)
        if usertType=='admin':
         print(usertType)
         return redirect('owner')
        else:
         productsData = Product.get_all_products()
         context = {'products': productsData}
         return render(request, 'Home.html', context)
    else:
          return redirect( 'login')

def owner(request):
    products = Product.get_owner_products(request)
    context = {'products': products}

    if 'ath' in request.session:
        auth = request.session['ath']
        token = auth['access']
        user = jwt.decode(token, options={"verify_signature": False})
        usertType = auth['userType']

        return render(request, 'OwnerProduct.html', context)
    else:
         return redirect('login')

def login(request):

    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def addproduct(request):
    if 'ath' in request.session:
        auth = request.session['ath']
        token = auth['access']
        user = jwt.decode(token, options={"verify_signature": False})
        usertType = auth['userType']

        context = {'owner': user['user_id']}
        return render(request, 'Addproduct.html', context)
    else:
         return redirect('login')

class AddProductView(APIView):
    #   renderer_classes = [UserRenderer]
    def post(self, request, format=None):

        serializer = ProductAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        if 'ath' in request.session:
            auth = request.session['ath']
            token = auth['access']
            user = jwt.decode(token, options={"verify_signature": False})
            usertType = auth['userType']

            return redirect('owner')
        else:
            return redirect('login')
