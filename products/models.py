from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from accounts.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image_url = models.CharField(max_length=200, validators=[URLValidator()])
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="products")
    def clean(self):
        super().clean()
        if not self.image_url.startswith("http://") and not self.image_url.startswith("https://"):
            raise ValidationError("Invalid image URL.")