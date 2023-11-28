from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Product

from base.serializers import ProductSerializer


from rest_framework import status

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all() #it returns all products objects from models.After completion of model setup we can apply this while serializing the data.
    serializer = ProductSerializer(products, many=True) #-We get error here like serializer so apply serialization.
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    
    
    return Response(serializer.data)