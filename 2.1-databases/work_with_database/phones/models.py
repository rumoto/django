from django.db import models

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

