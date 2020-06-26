from django.shortcuts import render, redirect
from main.models import Card
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random, os, base64
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def index(request):
    card_list = Card.objects.all().order_by('-date_now')
    return render(request, 'index.html', {'card_list':card_list})

def create(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    elif request.method == 'POST':
        new_card = Card.objects.create(
            contents = request.POST['contents'],
            templates = request.POST['templates'],
        )
        return redirect('/')

@csrf_exempt
def canvasToImage(request):
    data = request.POST.__getitem__('data')
    data = data[22:]
    number = random.randrange(1,10000)

    # path = str(os.path.join(settings.STATIC_ROOT, 'resultImg/'))
    path = staticfiles_storage.url('resultImg/')
    filename = 'image' + str(number) + '.png'

    image = open(path+filename, "wb")

    image.write(base64.b64decode(data))
    image.close()

    answer = {'filename': filename}
    return JsonResponse(answer)