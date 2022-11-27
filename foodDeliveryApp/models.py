from django.db import models
from userProfileApp.models import User

# Create your models here.
class FoodCategories(models.Model):
    CategoryName = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f"{self.pk}.{self.CategoryName}"

class FoodMenu(models.Model):
    Category = models.ForeignKey(FoodCategories, on_delete=models.CASCADE, related_name="foodCetegoryRelatedName")
    Name = models.CharField(max_length=250)
    Price = models.CharField(max_length=250)
    Subtitle = models.CharField(max_length=250)
    Image = models.ImageField(null=True, blank=True, upload_to="0_DynamicImages/Food_Image")

   
    def __str__(self):
        return f"{self.pk}.{self.Name}"

class PurchasedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="PurchasedItemUserRelatedName", null=True)
    customerName = models.CharField(max_length=264, null=True)

    #product info
    item = models.ForeignKey(FoodMenu, on_delete=models.CASCADE, related_name="PurchasedItemRelatedName")
    itemPrice = models.CharField(max_length=264, null=True, blank=True)
    quantity = models.CharField(max_length=264, null=True, blank=True)
    totalPrice = models.CharField(max_length=264, null=True, blank=True)

    #customer info 
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    post_office = models.CharField(max_length=250, null=True, blank=True)
    thana = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=264, null=True, blank=True)

    #transaction info
    transactionId = models.CharField(max_length=264, null=True)
    validationID = models.CharField(max_length=264, null=True)


    ORDER_STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
        
    ]

    OrderStatus = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, blank=True, null=True)


    def __str__(self):
        return f"{self.pk}.{self.customerName}" 
    
