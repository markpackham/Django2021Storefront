from django.urls import path
from . import views

# This is a URLConf module
urlpatterns = [
    # http://127.0.0.1:8000/playground/hello/
    # always end url with a "/"
    path('hello/', views.say_hello),
]