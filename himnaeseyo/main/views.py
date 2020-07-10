from django.shortcuts import render, redirect
from main.models import Photo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random, os, base64
from django.conf import settings

# Create your views here.

def home(request):
    photo_list = Photo.objects.all().order_by('-id')
    # randEnd = photo_list[0].id
    # print(randEnd)                                   
    # n = random.randrange(1, randEnd)                         
    return render(request, 'home.html', {'photo_list':photo_list})

def create(request):
    return render(request, 'create.html')

# ajax post 받아줌
@csrf_exempt
def cardImageSave(request):
    data = request.POST.__getitem__('data')
    # data:image/png;base64 제거
    data = data[22:]
    number = random.randrange(1,10000)

    # /himnaeseyo/main/static/resultImg/
    path = str(os.path.join(settings.STATIC_ROOT, 'resultImg/'))
    modelpath = 'resultImg/'
    # print("로그 잠시만 : " + path)

    filename = 'image' + str(number) + '.png'
    modelpath = modelpath + filename

    new_photo = Photo.objects.create(
            filename = filename,
            path = modelpath,
        )

    # "wb" 쓰기전용으로 파일을 open
    image = open(path+filename, "wb")
    # 'base64.b64decode()'를 통하여 디코딩을 하고 파일에 써준다.
    image.write(base64.b64decode(data))
    image.close()

    return JsonResponse({'filename': filename})