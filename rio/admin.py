from django.contrib import admin
from .models import Oder
from .models import User
from .models import Item
from .models import Message
# Register your models here.
admin.site.register(Oder)
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Message)
