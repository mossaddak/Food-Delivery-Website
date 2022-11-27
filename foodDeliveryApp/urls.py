from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('PageNotFound/', views.PageNotFound, name='PageNotFound'),
    path('AllFoodItem/', views.AllFoodItem, name="AllFoodItem"),
    path("QuickView/<int:pk>/", views.QuickView, name="QuickView"),
    path("OrderItem/<int:pk>/", views.OrderItem, name="OrderItem"),
    path("MakePayment/<int:pk>/", views.MakePayment, name="MakePayment"),
    path("Payment-Status/", views.PaymentStatus, name="PaymentStatus"),
    path("PurchasedProduct/<tran_id>/<val_id>/", views.PurchasedProduct, name="PurchasedProduct")
]  