from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Product


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
