from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('cart-page/', views.cart_page, name='cart_page'),
    path('tracker/', views.tracker, name='tracker'),
    path('watches/', views.watches, name='watches'),
    path('shoes/', views.shoes, name='shoes'),
    path('mobile-accessories/', views.mobile_accessories, name='mobile_accessories'),
    path('caps/', views.caps, name='caps'),
    path('product/<int:prid>/', views.product_page, name='product_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)