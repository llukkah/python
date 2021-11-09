from django.urls import path
from . import views

urlpatterns = [
    # this route serves sandwich homepage
    path('', views.sandwich, name = 'sandwich'),
    path('ingredients/<str:ingredient_type>/', views.ingredients_list, name = 'ingredients_list'),
    path('random', views.sandwich_generator, name='sandwich_generator')
]