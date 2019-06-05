from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo,HeroInfo
from django.template import loader

# Create your views here.

def index(req):
    temp = loader.get_template('index.html')
    res = temp.render({})
    return HttpResponse(res)
def list(req):
    books = BookInfo.objects.all()
    print(books)
    temp = loader.get_template('list.html')
    res = temp.render({'books':books})
    return HttpResponse(res)
def detail(req,id):
    book = BookInfo.objects.get(pk=id)

    temp = loader.get_template('detail.html')
    res = temp.render({'book':book})
    return HttpResponse(res)