from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CreateUser, LodinForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my-login.html')

def home(request):
    return render(request, 'index.html', )


def createTask(request):
    form=TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-task')

    context ={'form': form}
    return render(request, 'create-task.html', context=context)


def viewTasks(request):
    tasks = Task.objects.all()

    context ={'tasks': tasks}
    return render(request, 'view-task.html', context=context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-task')

    context ={'form': form}

    return render(request, 'update-task.html', context=context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('view-task')

    context={'object':task}

    return render(request, 'delete-task.html', context=context)







def register(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registared!')
        
    context = {'form': form}
    return render(request, 'register.html', context=context)



def my_login(request):
    form = LodinForm()
    if request.method == 'POST':
        form = LodinForm(request, data=request.POST)
        if  form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'my-login.html', context=context)

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    auth.logout(request)
    return redirect('index')
    
