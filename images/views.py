from django.http import JsonResponse
from .models import Image


def root(request):
    output = {
        "images": [{
            "name": img.name,
            "original_url": img.original.url,
            "thumbnail_url": img.thumbnail.url,
            } for img in Image.objects.all()]
    }
    return JsonResponse(output)
