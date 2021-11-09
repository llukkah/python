from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def hello(request):
    if request.method =='GET':
        return render(request=request, template_name='hello.html')

def hello_name(request, name):
    if request.method =='GET':
        return render(request=request, template_name='hello_name.html', context={'name': name})