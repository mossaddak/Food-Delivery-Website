from django.db import models
from django.conf import settings

# Create your models here.

class BilligAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=264)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username} billing address'

    def is_fully_filld(self):
        fields_name = [f.name for f in self._meta.get_fields()]

        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        
        return True

    class MEta:
        verbose_name_plural = "Billing Adresses"