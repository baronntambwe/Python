from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dic = {'help_me': "Hello, I need help from help.html"}
    return render(request, "help.html", context=my_dic)
