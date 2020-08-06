from django.http import JsonResponse
from django.shortcuts import render

from .models import Product


def product_view(request):
    result = {
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "value": p.value,
                "discount": p.discount,
                "stock": p.stock,
            }
            for p in Product.objects.all()
        ]
    }
    return JsonResponse(result)
