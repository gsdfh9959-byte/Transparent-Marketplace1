from django.shortcuts import render
from .models import Product

def product_list(request):
    # Получаем ВСЕ товары из базы данных
    products = Product.objects.filter(is_available=True).order_by('-created_at')
    
    # Передаём товары в шаблон
    return render(request, 'products/list.html', {'products': products})