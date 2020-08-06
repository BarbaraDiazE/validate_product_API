from django.http import JsonResponse
from django.shortcuts import render


def validation_view(request):
    result = {"products":
              [
                  {"id": "L_120", "name": "Leche",
                   "value": 10.00, "discount": 0.10, "stock": 5},
                  {"id": "G_100", "name": "Galletas",
                   "value": 8.00, "discount": 0.10, "stock": 15}
              ]
              }
    return JsonResponse(result)
