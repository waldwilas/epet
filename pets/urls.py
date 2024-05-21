from django.urls import path

from . import views


app_name = 'pets'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_pet, name='add'),
    path('<int:id>/', views.show_pet, name='show'),
    path('<int:id>/edit', views.edit_pet, name='edit'),
    path('<int:id>/delete', views.delete_pet, name='delete'),
]
