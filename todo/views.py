from django.shortcuts import render,HttpResponse,redirect
from .models import  Todo
# Create your views here.

def homepage(request):
    todos = Todo.objects.all()
    return render(request,"index.html",{"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("admin/")
    else:
        title = request.POST.get("todotitle")
        newTodo = Todo(title = title,completed=False)
        newTodo.save()
        return redirect("/")

def updateTodo(request,id):
    todo = Todo.objects.filter(id=id).first()
    todo.completed = not todo.completed  
    todo.save()
    return redirect("/")

def deleteTodo(request,id):
    todo = Todo.objects.filter(id=id).first()
    todo.delete()
    return redirect("/")