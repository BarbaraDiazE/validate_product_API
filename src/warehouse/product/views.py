from django.http import JsonResponse
from django.shortcuts import render


def validation_view(request):
    product = {"id": "A_120", "name": "Leche",
               "value": 10.00, "discount": 0.10, "stock": 5}
    return JsonResponse(product)
