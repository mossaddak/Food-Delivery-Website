from django.contrib import admin
from .models import (
    FoodCategories,
    FoodMenu,
    PurchasedItem
)

class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("CategoryName",)

class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ("Name", "Price", "Subtitle", "Category","Image",)

class PurchasedItemAdmin(admin.ModelAdmin):
    list_display = (
        "customerName",
        "item",
        "itemPrice",
        "quantity",
        "totalPrice",
        "phone_number",
        "post_office",
        "thana",
        "district",
        "zipcode",
        "address",
        "transactionId",
        "validationID",
        "OrderStatus",
    )

# Register your models here.
admin.site.register(FoodCategories, FoodCategoryAdmin)
admin.site.register(FoodMenu, FoodMenuAdmin)
admin.site.register(PurchasedItem, PurchasedItemAdmin)
