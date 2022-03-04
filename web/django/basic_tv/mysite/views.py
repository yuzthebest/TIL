from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')


def lunch(request):
    menus = ['설렁탕', '곱창', '회', ' 똠양꿍']
    menu = random.choice(menus)
    context = {
        'menu' : menu,
    }
    return render(request, 'mysite/happy.html', context)

def lotto(request):
    lucky_numbers = random.sample(range(1,46), 6)
    context = {
        'lucky_numbers' : lucky_numbers,
    }
    return render(request, 'mysite/lotto.html', context)

def greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'mysite/greeting.html', context)
