from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    @permission_classes([IsAuthenticated])
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPIView(APIView):
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)
    
    permission_classes = [IsAuthenticated]

    def put(self,request,productId):
        user = request.user
        product = self.get_object(productId)
        if user == product.user:
                serializer = ProductSerializer(product,data=request.data,partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
    def delete(self,request,productId):
        user = request.user
        product = self.get_object(productId)
        if user == product.user:
            product.delete()
            data = {"pk": f"{productId} is deleted."}
            return Response(data,status=status.HTTP_200_OK)