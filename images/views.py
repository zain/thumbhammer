from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Image


@csrf_exempt
def root(request):
    if request.method == "POST":
        Image.objects.create(
            name=request.POST['name'],
            original=request.FILES['file'],
        )

    output = {
        "images": [{
            "name": img.name,
            "original_url": img.original.url,
            "thumbnail_url": img.thumbnail.url if img.thumbnail else "",
            } for img in Image.objects.all()]
    }
    return JsonResponse(output, json_dumps_params={'indent': 2})
