from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from .models import *
# Create your views here.

class MainView(View):
    def get(self,req):
        return render(req,'main.html')

class IndexView(View):
    def get(self,req):
        return render(req,'index.html')

class FormView(View):
    def get(self,req):
        return render(req,'form.html')

class TableView(View):
    def get(self,req):
        article = Summary.objects.all()
        return render(req,'table.html',locals())

class LoginView(View):
    def get(self,req):
        return render(req,'login.html')

class RegisterView(View):
    def get(self,req):
        return render(req,'register.html')


from django.http import HttpResponse
class NavView(View):
    def get(self,req):
        # return HttpResponse("hhh")
        return render(req,'nav.html',locals())