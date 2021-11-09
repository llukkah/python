from django.urls import path
from hello.views import hello, hello_name

urlpatterns = [
    path('', hello, name='hello'),
    path('<str:name>', hello_name, name='hello_name')
]