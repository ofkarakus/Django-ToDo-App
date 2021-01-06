from django.shortcuts import get_object_or_404, render
from main_app.models import Todo
from main_app.forms import TodoForm

# Create your views here.


def display_home_page(request):
    return render(request, 'main_app/home_page.html')


def display_todo_list(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'main_app/todo_list.html', context)


def display_todo_details(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_form = TodoForm(instance=todo)
    context = {
        'todo_form': todo_form
    }

    return render(request, 'main_app/todo_details.html', context)
