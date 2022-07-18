from rest_framework import serializers
from store.models import Product


from account.utils import Util


class AddProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description' , 'user']

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)



