from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import pandas as pd
from .models import Task, StatusMaster, CategoryMaster
from .forms import TaskForm
from pprint import pprint

# Create your views here.
def index_view(requests):
    objects = pd.DataFrame(Task.objects.all().values('id', 'sr_no', 'title', 'category', 'status', 'created_at', 'updated_at'))
    col_names = {
        'sr_no' : "Serial No.",
        'category' : "Category",
        'status' : "Status",
        'title': "Task Title",
        'created_at': "Created At",
        'updated_at' : "Updated At"
    }
    # objects.rename(columns=col_names, inplace=True)
    columns = objects.columns.to_list()
    object_list = objects.to_dict('records')
    form = TaskForm(requests.POST or None)
    cdict = {
        'columns' : columns,
        'object_list' : object_list,
        'form' : form,
    }
    return render(requests, "index.html", cdict)


# view to add a new task
def add_task(requests):
    print(f"Add task called : {requests.method}")
    form = TaskForm(requests.POST or None)
    task = None
    task = Task.objects.all().order_by('-sr_no').first()
    if requests.method == "POST":
        if form.is_valid():
            print(f"Form is Valid")
            form.instance.sr_no = task.sr_no+1 if task else 1
            form.save()
            return redirect("/")
        else:
            print("Form is not valid")
            messages.error(requests, form.errors)
    cdict = {
        'form' : form,
        'task' : "add"
    }
    return render(requests, "add_task.html", cdict)


# view to edit task
def edit_task(request, pk:str):
    obj = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            print(f"Form is Valid")
            obj.status = form.cleaned_data["status"]
            obj.category = form.cleaned_data["category"] if form.cleaned_data["category"] is not None else None
            obj.description = form.cleaned_data["description"]
            obj.title = form.cleaned_data["title"]
            obj.save()
            return redirect("/")
        else:
            print("Form is not valid")
            pprint(form.errors)
            messages.error(request, form.errors)
            return render(request, "add_task.html", {'form' : form, 'task' : "edit"})
    else:
        form = TaskForm(instance=obj)
        return render(request, "add_task.html", {'form' : form, 'task' : "edit"})

def delete_task(requests, pk:str):
    try:
        obj = Task.objects.get(pk=pk)
        obj.delete()
        print(f"Object deleted")
    except Exception as e:
        print(f"Exception deleting : {str(e)}")
        return redirect("/")
    return redirect("/")
    