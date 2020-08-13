import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return HttpResponse('こんにちは、世界！')


def temp(request):
    context = {'msg': 'こんにちは、世界！'}
    return render(request, 'main/temp.html', context)


def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })


def iftag(request):
    return render(request, 'main/iftag.html', {
        'random': random.randint(0, 100)
    })


def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': None
    })


def firstof(request):
    return render(request, 'main/firstof.html', {
        # 'a': 'おはよう',
        # 'b': 'こんにちは',
        'c': 'こんばんは',
    })


def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月', '火', '水', '木', '金', '土', '日']
    })


def forempty(request):
    return render(request, 'main/forempty.html', {
        # 'members': ['鈴木', '佐藤', '山田']
    })


def escape(request):
    return render(request, 'main/escape.html', {
        'msg': '''<img src="https://wings.msn.to/image/wings.jpg" title="logo" />
        <p>WINGSへようこそ</p>'''
    })


def master(request):
    return render(request, 'main/master.html', {
        'msg': 'こんにちは、世界！',
    })


def include(request):
    return render(request, 'main/include.html', {
        'name': '鈴木',
        'current': datetime.datetime.now(),
    })
