from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home_page, name='home'),
    path('todo_list/', views.display_todo_list, name='todo_list'),
    path('todo/<int:id>/details', views.display_todo_details, name='todo_details'),
    path('todo/<int:id>/delete', views.delete_todo, name='delete_todo'),
    path('add_todo/', views.add_todo, name='add_todo')
]
