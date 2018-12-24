from django.db import models
from django.conf import settings
from django.utils import timezone

class User (models.Model):
    user_name = models.CharField(max_length = 20)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.user_name

class Oder(models.Model):
    quontity = models.IntegerField()
    note = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    deliverd_time = models.DateTimeField(blank=True , null=True)
    is_delivered = models.BooleanField(default=False)
    users = models.ForeignKey(User,related_name='username', on_delete=models.CASCADE)

    def delivered(self):
        self.is_delivered = True
        self.save()

    def __str__(self):
        return self.note

    def delivered_orders(self):
        return self.Orders.filter(is_delivered=True)



class Item(models.Model):
    name = models.CharField(max_length = 50)
    oders = models.ForeignKey(Oder, on_delete=models.CASCADE , related_name = 'order_items')
    price = models.IntegerField()
    pic_link = models.CharField(max_length=70)

    def __str__(self):
        return self.name

# oders object
