from django.db import models

# Create your models here.

class Item(models.Model):
    choice = (
        ("bakery", "bakery"),
        ("meat", "meat"),
        ("healthy living", "healthy living"),
        ("baby care", "baby care"),
        ("health wellness", "health wellness"),
        ("home cleaning", "home cleaning"),
        ("cooking essentials", "cooking essentials"),
        ("fruit vegetable", "fruit vegetable"),
        ("other", "other")
    )
    name = models.CharField(max_length=150, null=True)
    price = models.IntegerField(null=True)
    category = models.CharField(choices=choice, default="other", max_length=150)
    description = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = "items"