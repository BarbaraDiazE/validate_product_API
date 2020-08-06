import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .validators import validate_fields, validate_products


@csrf_exempt
def product_view(request):
    if request.method == "GET":
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
        return JsonResponse(result, status=200)
    return HttpResponse(status=405)


@csrf_exempt
def products_bulk_insert(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        if "products" in payload:
            products = payload["products"]
            error_counter = validate_fields(products)
            products_report = validate_products(products)
            if (error_counter == 0) and (not products_report):
                result = {"status": "OK"}
                return JsonResponse(result, status=200)
            error_response = {
                "status": "ERROR",
                "products_report": products_report,
                "number_of_products_unable_to_parse": error_counter,
            }
            return JsonResponse(error_response, status=422)

        return HttpResponse(status=400)
    return HttpResponse(status=405)
