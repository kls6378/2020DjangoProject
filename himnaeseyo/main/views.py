from django.shortcuts import render, get_object_or_404
from main.models import Card
# Create your views here.

def index(request):
    # card_list = Card.
    return render(request, 'index/index.html')