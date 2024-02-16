from rest_framework import serializers
from .models import CustomerAuth, AdminProducts

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = CustomerAuth
        fields = ('__all__')

class AdminSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    condition = serializers.CharField(max_length=100)
    noofdays = serializers.IntegerField()
    category = serializers.CharField(max_length=200)
    options = serializers.JSONField()
    rentaloptions = serializers.JSONField()

    class Meta:
        model = AdminProducts
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'category': {'required': True},
            'noofdays': {'required': True}
        }