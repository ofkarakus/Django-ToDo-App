from django.shortcuts import get_object_or_404, redirect, render
from main_app.models import Todo
from main_app.forms import TodoAddForm, TodoUpdateForm

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
    todo_update_form = TodoUpdateForm(instance=todo)

    # update todo details
    if request.method == 'POST':
        todo_updated_form = TodoUpdateForm(request.POST, instance=todo)
        if todo_updated_form.is_valid():
            todo_updated_form.save()
            return redirect("todo_list")

    context = {
        'todo_update_form': todo_update_form,
        'todo': todo
    }

    return render(request, 'main_app/todo_details.html', context)


def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    context = {
        'todo': todo
    }

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')

    return render(request, 'main_app/delete_todo.html', context)


def add_todo(request):
    todo_add_form = TodoAddForm()
    context = {
        'todo_add_form': todo_add_form
    }

    if request.method == 'POST':
        new_todo = TodoAddForm(request.POST)
        if new_todo.is_valid():
            new_todo.save()
            return redirect('todo_list')

    return render(request, 'main_app/add_todo.html', context)
