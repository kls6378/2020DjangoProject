from django.shortcuts import render, redirect
from main.models import Card

# Create your views here.

def index(request):
    card_list = Card.objects.all().order_by('-date_now')
    return render(request, 'index.html', {'card_list':card_list})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        new_card = Card.objects.create(
            contents = request.POST['contents'],
            templates = request.POST['templates'],
        )
        return redirect('/')
