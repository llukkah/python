urls.py - all urls you want to handle in the django server.  defines roots.  everytime you add new pages you need to add them here.

views.py - interacts to the models.py
    every function in this file, serves a different page / set of pages

    renders specific pages depending on the url that's called

defines the urls and calles the method in views.py

models.py - 

urls.py <-> views forwards request to approriate view in views.py



client <-> server/django    <--------------------
                |               models.py       | 
                |               ^               |
     HTTP       |               | read/write    |
    request     |               |  data         |   
                v               v               |
                urls.py ----> views.py----------
                                ^
                                | 
                                |
                                template.html 

1. set up virtual environment/django
    # pip3 freeze > requirements.txt whenever you install new packages
2. Create Project: 
    in virtual env # django-admin startproject PROJECT NAME (mysite)
3. CD PROJECT NAME directory
4. Create app: 
    # python manage.py startapp GIVE APP NAME(hello)

5. cd hello
6. IN VS CODE: Register app w/ project :
    #go to settings.py file
    # under installed_apps add  'hello.apps.HelloConfig'
    ^^installs the app for us
7. Migrate in TERMINAL: 
    # cd into PROJECTNAME DIR 
    # then: python manage.py migrate
8. Create SuperUser(admin): #python manage.py createsuperuser
    ---default username, false email, simple password.
    hello@llukkah.com
    llukkah
    1234
9. run server: # python manage.py runserver
10. VS CODE - hello/appName directory: # create urls.py
11. in views.py
    from django.shortcuts import render

    #create views here
    def hello(request):
        if request.method =='GET':
        return render(request=request, template_name='hello.html')

    def hello_name(request, name):
        if request.method =='GET':
            return render(request=request, template_name='hello_name.html', context={'name': name})
12. in urls.py:
    from django.urls import path
    from hello.views import hello, hello_name

    urlpatterns = [
        #creating initial page that's /hello/
        path('', hello, name='hello'),
        path('<str:name>', hello_name, name='hello_name')
        # 3 arguments - define what path should be, what you want to call 'you', what you want to call the URL
    ]
13. Create new directory in HELLO directory: 
    # mkdir "templates"
    must be named templates, python/django is expecting this
14. in Templates # touch hello.html
15. in hello.html: <h1>Hello World</h1>
16. in mysite dir - open urls.py file
    second line: 
        # from django.urls import path, include
    under urlpatterns, add:
        # path('hello/', include('hello.urls'))

17. in Templates dir :
    # touch hello_name.html
    <h1>Hello {{ name }}</h1>


# NOTE: in local host `/admin` takes you to admin page to look into various databases