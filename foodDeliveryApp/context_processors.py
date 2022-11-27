from .models import FoodCategories


def categories(request):
    return {"foodCategory":FoodCategories.objects.all()}