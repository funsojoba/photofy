from django.shortcuts import render
from .models import Photo



def index(request):
    if request.method == 'POST':
        new_image = Photo.objects.create(photo=request.FILES['img'])
        context = {
            "url": new_image.photo.url,
        }
        return render(request, "photofy/index.html", context)
        
    return render(request, 'photofy/index.html')