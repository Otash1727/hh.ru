from django.shortcuts import get_object_or_404
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from wildberries.models import Products
from .serializers import ProductSerializer
from apscheduler.schedulers.background import BackgroundScheduler

class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        article = request.data.get('article')
        if not article:
            return Response({"error": "Article is required"}, status=400)

        self.update_or_create_product(article)
        product = Products.objects.get(article=article)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=201)

    def update_or_create_product(self, article):
        url = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch product data for article {article}")

        data = response.json()
        product_data = data['data']['products'][0]

        product, created = Products.objects.update_or_create(
            article=article,
            defaults={
                'name': product_data['name'],
                'price': product_data['salePriceU'] / 100,
                'rating': product_data['rating'],
                'quantity': product_data['totalQuantity'],
            }
        )
        return product

    def get(self, request, article=None):
        if article:
            product = get_object_or_404(Products, article=article)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)


def update_all_products():
    products = Products.objects.all()
    for product in products:
        try:
            ProductCreateView().update_or_create_product(product.article)
            print(f"Product {product.article} updated successfully.")
        except Exception as e:
            print(f"Failed to update product {product.article}: {e}")
