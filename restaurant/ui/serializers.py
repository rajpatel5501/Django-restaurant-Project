from rest_framework import serializers
from store.models import Product


class ProductAddSerializer(serializers.ModelSerializer):


  class Meta:
    model = Product
    fields=['name', 'description', 'price', 'user']
 

  def validate(self, attrs):

    return attrs

  def create(self, validate_data):
    return Product.objects.create(**validate_data)