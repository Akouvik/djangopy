from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',{'all_items':all_todo_items})


#adds an item to the todolist by calling the TodoItem class with the content typed in
def addTodo(request):
    new_item = TodoItem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    #create a new todo all_items
    #save
    #redirect teh browser to '/todo/'