Models - Many to Many Relationships
in django projects dir:
1. activate virtual environment
2. Create app: python manage.py startapp blog
3. mysite/settings.py >> 'blog.apps.BlogConfig'
4. mysite/urls.py >>
    from django.urls import path
    urlpatterns = [
        path('blog/', include('blog.urls'))
    ]

5. blog/urls.py >>
        from django.urls import path
        from . import views
    urlpatterns = [
path('', views.blog, name='blog')
path('edit/<int:post_id', name='edit')
    ]
6.blog/models.py >>
    from django.db import models
        class Tag(models.Model):
            tag_id = models.AutoField(primary_key=True)
            name = models.CharField(max_length=255)

        class Post(models.Model):
            post_id = models.AutoField(primary_key=True)
            img_link = models.URLField()
            title = models.CharField(max_length=255)
            body = models.TextField()
            tags = models.ManyToManyField(Tag
            )

7. Make migrations and Migrate>>
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
8. Register models in blog/Admin.py >> 
    from django.contrib import admin   
    from .models import *
    admin.site.register(Post)
    admin.site.register(Tag)

    ***in admin site, you should see the Blog / Posts / Tags options appear

9. In admin site, make Tags >>
    Tags > Click Add > Travel, Digital Nomad, Location Freedom

    Make Blog Post >> 

10. stop server
11. run python shell >> python3 manage.py shell
    from blog.models import Post
    Post.objects.create(title = 'Paul post 3', body = 'content here', img_link = 'url here')

    ***this will make a new blog post in the terminal, instead of doing it on the admin site

12. exit shell >> exit()

13. blog/views.py >>
    from django.shortcuts import render
    from .models import Post, Tag

    def blog(request):
        posts = Post.objects.all(order_by('-pose_id'))
        return render(request=request, template_name='blog.html', context={posts})
    ^^not complete

    def edit(request, post_id):
        if request.method == 'GET':
            post = Post.objects.get(pk=post_id)
            tags = []
            for tag in post.tags.all():
                tags.appent(tag.tag_id)
            form = EditorForm(initial={
                'title': post.title,
                'img_link': post.img_link,
                'body': post.body
                'tags': tags,
            })
        posts = Post.objects.all(order_by('-post_id'))
        return render(request=request, template_name='edit.html', context={'post_id' = post_id})

14. templates/blog.html::
    <h1>Blog</h1>
    <{% for post in posts %}
    <div>
    <img src="{{post.img_link }}"/>
    <a href="">Edit Post</a>
    <h2>{{ post.title }} </h2>
    <p> {{post.body}}</p>
    <div {% for tag in post.tags.all%}
    <span>{{tag.name}}</span>
    {% end for%}
    </div>
    </div>
    {% end for %}

15. blog/forms.py::

from django import forms
from .models import Tag
class EditorForm(forms.Form):
    title = forms.ChjarField(max_length=255)
    img link = forms.URLField()
    body = forms.CharField(widget=forms.Textarea)
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
        tags = forms.MultipleChoiceField(widget-forms.CheckboxSelect.;...)

16. templates/edit.html
<h1> edit post</h1>
<form action"{ % url 'edit' post_id % }" method="POST">
{% csrf_token %} {{ form }}
<input type="submit" name="save" value="Save" />
<input type="submit" name="delete" value="Delete" />
</form>