from django.urls import path
from . import views

app_name = 'djRecipes'

urlpatterns = [
    path('', views.recipes, name='list'),
    path('<int:id>/', views.recipeDetails, name='detail'),
]
