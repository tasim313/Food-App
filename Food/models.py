from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=555, default='https://media.istockphoto.com/vectors/fast-food-vector-card-with-text-placeholder-vector-frame-with-fast-vector-id1131995796')

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("Food:item-details", kwargs={"pk":self.pk})

