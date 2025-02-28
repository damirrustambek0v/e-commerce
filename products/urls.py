from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, OrderListCreateView, OrderDetailView, ProductListCreateView, ProductDetailView, OrderItemListCreateView, OrderItemDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orderitems/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
]
