from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomerAuth, AdminProducts
from .serializers import CustomerSerializer, AdminSerializer
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.

####
class AlldataView(APIView):
    def get(self, request, *args, **kwargs):
        results = CustomerAuth.objects.all()
        serializer = CustomerSerializer(results, many=True)
        return Response ({'status': 'Success', 'Customers_data': serializer.data}, status=200)

####
class LoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        serializer = CustomerSerializer(data=request.data)
        # username, password = request.data['username'], request.data['password']
        
        customer = CustomerAuth.objects.filter(username=request.data['username'], password=request.data['password'])
        
        if not customer:
            return Response ({'status': 'error', 'Error': 'Invalid Credentials'}, status=400)
        else:
            return Response ({'status': 'Success', 'text': 'Login Successfull'}, status=200)
        
        
####
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response ({'status': 'Registered Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        else: 
            return Response({'status': 'Error', 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)


###
        
class AdminView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response ({'status': 'Categories Added Successfully', "categories": serializer.data }, status=status.HTTP_200_OK)
        else:
            return Response ({'status': 'Error', 'Error': 'Missing Fields'}, status=status.HTTP_400_BAD_REQUEST)


###

class GetAllFurView(APIView):
    def get(self, request, *args, **kwargs):
        result = AdminProducts.objects.all()
        serializer = AdminSerializer(result, many=True)
        return Response ({"status": 'success', "Furnitures": serializer.data}, status=status.HTTP_200_OK)


class GetFurbyCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        category = kwargs.get('category')
        if category:
            categories = AdminProducts.objects.filter(category=category)  
            serializer = AdminSerializer(categories, many=True)  
            return Response(serializer.data)
        






































