from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductCreateView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductCreateView.as_view(), name='product_list'),  # List all products
    path('products/<str:article>/', ProductCreateView.as_view(), name='product_detail'),  # View a single product by article
]


