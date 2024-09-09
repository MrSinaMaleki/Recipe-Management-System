from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name='index'),

    path('recipes/', views.recipe_list, name='recipe_list'),
    path('create_recipe/', views.recipe_create, name='recipe_create'),
    path('delete_recipe/<int:pk>', views.recipe_delete, name='recipe_delete'),
    path('update_recipe/<int:pk>', views.recipe_update, name='recipe_update'),

]
