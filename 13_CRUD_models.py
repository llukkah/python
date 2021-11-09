To Do List App
# - Models - way of creating tables without writing SQL
#when making models in django, you are creating a CLASS

-activate python - source django-env/bin activate
-python3 manage.py startapp todo
-register django project:
    mysite/settings.py:
        'todo.apps.TodoConfig'
-MYSITE/URLS.PY
    path('todo/', include('todo.urls'))

-in todo dir:
    touch urls.py

- TODO/URLS.PY
    from django.urls import path
    urlpatterns = [

    ]
- TODO/MODELS.PY
    from django.db import models
    # inherites models.Model from django
    class Todo(models.Model):
        task_id = models.AutoField(primary_key=True)
        task = models.CharField(max_length=255)

- TODO/ADMIN.PY:
    #register models in this file
    from django.contrib import admin
    from . import models
    #allows admin user to work w this model
    admin.site.register(models.Todo)

- In terminal:
    # python3 manage.py makemigrations
    -use this whenever you change anything about your models in models.py file - anything CRUD of your classes
    # python3 manage.py migrate
- run server :
    # python3 manage.py runserver
    # go to admin page and sign in.

- In admin page: #this is creating your DB from admin page
    # click add to your ToDo
    # teach JTC class
    # learn CSS
    # learn django

- OPTIONAL for DEBUGGING / EXPLORING: 
    In terminal:
    python3 manage.py shell
    # this explores the TODO objects that we have n see how it's organized, and how we can acess them.
    from todo.models import todo
    Todo.objects.all()
    # this gives all the objects of the ToDo model we made in the admin site.
    Todo.objects.create(task='learn about models')
    #delete.. deletes the task, but doesnt renumber the remaining objects
    Todo.objects.filter(pk=3).delete


    Queryset API:
    # use python syntax to query the objects we created
        Todo.objects.all()[0] - returns first item
        Todo.objects.all()[0].task_id
        Todo.objects.all()[0].task
        Todo.objects.filter(task='learn css') - returns a specific object you made

    exit()
- TODO/URLS.PY
    from django.urls import path
    from . import views

    urlpatterns = [
        #todo/
        path('', videw.todo, name= 'todo')

    ]
- bring in the MODEL: TODO/VIEWS.PY
    from django.shortcuts import render
    from .models import Todo #now we have access of the Todo class in our views.py file

    def todo(request):
        if request.method == 'GET':
            # creating tasks from our Todo objects we made
            #tasks is our Queryset of Todo objects
            # context - passing the tasks as a variable to be used in HTML file
            tasks = Todo.objects.all()
            return render(request = request,
            template_name = 'list.html', context = {'tasks': tasks})

- mkdir templates, touch list.html:
    <h1>Tasks Todo</h1>
    <ul>
    {% for task in tasks %} 
    <li><a href="">{{ task.task }}</a></li>  
    {% end for %} 
    </ul>

- create forms.py in TODO dir:
    from django import forms

    class TodoForm(forms.Form):
        task = forms.CharField(label='Add a Task', max_length=255)
    
- in list.html:
#    <h1>Tasks Todo</h1>
    <form action="{% url 'todo' %}" method="POST">
    #authentication type token.  need this to make post request to django 
    {% csrf_token %} {{ form }}
    <input type='submit' name='create' value = 'Create/'>

    </form>
#   <ul>
 #   {% for task in tasks %} 
 # <li><a href="">{{ task.task }}</a></li>  
   # {% end for %} 
    #</ul>

- in TODO/VIEWS.PY
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from .forms import TodoForm

#    def todo(request):
#       if request.method == 'GET':
#            tasks = Todo.objects.all()
            form = TodoForm()
           return render(request = request,
            template_name = 'list.html', context = {'tasks': tasks, 'form': form})
        
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                #add new Todo object to Queery Set
                Todo.objects.create(task=task)
                # reloading page afer we add new object to "refresh the list"
            return HttpResponseRedirect(reverse('todo'))

-UPDATE/DELETE Tasks:
    -TODO/URLS.PY:
    #url = todo/<int:task_id>
        path('int:task_id', views.task, name='task')
    -TODO/VIEWS.PY:
        def task(request, task_id):
            if request.method = 'GET':
                #looking up specific object by PK
                todo = Todo.objects.get(pk=task_id)
                #make a form, pre-populate the character field w name of task
                form = TodoForm(initial = {'task': todo.task})
                return render(request = request, template = 'detail.html', context = {'form': form, 'task_id':task_id})
            if request.method == 'POST':
                if 'save' in request.POST:
                    form = TodoForm(request.POST):
                    if form.is_valid():
                        # update task attribute of the task of the correct task_id the user inputs
                        task = form.cleaned_data['task']
                        Todo.objects.filter(pk=task_id).update(task=task)
                elif 'delete' in request.POST:
                    Todo.objects.filter(pk=task_id).delete()
                return HttpResponseRedirect(reverse('todo'))

    -TODO/detail.html:
        <form action="{% url 'task' task_id %}" method="POST"> 
    {% csrf_token %} {{ form }}
    <input type='submit' name='save' value = 'Save/'>
    <input type='submit' name='delete' value = 'Delete/'>
    </form>

    -TODO/list.html:
    # not complete
     <li><a href="{% url %}">{{ task.task_id }}</a></li>  