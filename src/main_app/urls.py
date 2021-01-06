from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home_page, name='home'),
    path('todo_list/', views.display_todo_list, name='todo_list'),
    path('todo/<int:id>/details', views.display_todo_details, name='todo_details')
]
