1. activate virtual env
    # source django-env/bin/activate
2. cd mysite dir
3. Make a new app: 
    # python3 manage.py startapp sandwich
4. In mysite/settings.py:
    installed_apps:
    # 'sandwich.apps.SandwichConfig'
5. In mysite/urls.py > urlpatterns:
    # path('sandwich/', include('sandwich.urls'))
6. In sandwich dir:
    # touch urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
       # this route serves sandwich homepage
        path('', views.sandwich, name = 'sandwich')
    ]

7. In sandwich/views.py:
    def sandwich(request):
        if request.method == 'GET':
            return render(request=request, template_name = 'sandwich.html', context = {'ingredients': ingredients.keys()})

# context : what is passed to the HTML
# context can be any data type in python

8. In Sandwich folder:
    # mkdir templates

9. In Templates dir:
    # touch sandwich.html

10. In Sandwich.html:
    <h1>Sandwich Home</h1>
    <h3>Ingredients List</h3>
    <ul>
        {% for ingredient in ingredients %}
        <li>
            <a href="/sandwich/ingredients/{{ ingredient }}">{{ ingredient }}</a>
        </li>
        {% endfor %}
    </ul>

    <form action='/sandwich/random'>
        <input type='submit' value='Make a random sandwich'/>
    </form>
11. In sandwich/urls.py:
    make ingredient routes:
        # path('ingredients/<str:ingreditent_type>/', views.ingredients_list, name = 'ingredients_list')

12. In sandwich/views.py:
ingredients = {
    'meats': ['ham', 'salami', 'turkey', 'chicken', 'meatball', 'tempeh'],
    'cheeses': ['cheddar', 'provolone', 'swiss', 'gyuere'],
    'toppings': ['lettuce', 'tomatoe', 'onion', 'pickles', 'peppers' ]
}
    # def ingredients_list(request, ingredient_type):
    if request.method =='GET': 
        return render(request=request, template_name='ingredients_list.html', context={ 'ingredients': ingredients[ingredient_type], 'ingredient_type': ingredient_type})

13. In templates: 
    #touch ingredients_list.html:
    <h1>{{ ingredient_type }}</h1>
    <ul>
        {% for ingredient in ingredients %}
        <li> {{ ingredient }}</li>
        {% endfor %}
    </ul>

14. Creating custom error message:
    in sandwich/view.py:
    from django.http import Http404
    #edit this function
    def ingredients_list(request, ingredient_type):
    if request.method =='GET': 
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient')
        return render(request=request, template_name='ingredients_list.html', context={ 'ingredients': ingredients[ingredient_type], 'ingredient_type': ingredient_type})

15. Random Sandwich Generator
    sandwich/urls.py:
    # path ('random', views.sandwich_generator, name='sandwich_generator')

16. in sandwich/views.py:
    import random
    def sandwich_generator(request):
        if request.method =='GET':
            selected_meat = random.choice(ingredients['meats'])
            selected_cheese = random.choice(ingredients['cheeses'])
            selected_topping = random.choice(ingredients['toppings'])

            sandwich = f'{selected_meat} & {selected_cheese} with {selected_topping}'

            return render(request=request, template_name="sandwich_generator.html", context = {'sandwich': sandwich})

17. In templates: 
    # touch sandwich_generator.html:
    <h1> {{ sandwich }} </h1>
    <p>Keep refreshing if you want a new sandwich</p>

NOTE: Make Dynamic URLS:

<a href="{% url 'ingredients_list' ingredient %}" </a>
Run Server:
    # python3 manage.py runserver
