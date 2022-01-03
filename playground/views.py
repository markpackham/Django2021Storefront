from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# "view" is a very missleading name since it is more of a "request handler" or "action"
# in Django a user never sees the "view" they just see templates

def say_hello(request):
    return render(request, 'hello.html', {'name':'Billy'})