from django.shortcuts import render
from .models import Item
# Create your views here.
def home_page(request):
    bites = Item.objects.filter(is_adrink=False)
    drinks = Item.objects.filter(is_adrink=True)
    return render(request, 'rio/index.html', {'drinks':drinks,'bites':bites})
