from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect, render_to_response, RequestContext,
)

from .forms import LoginForm


def login_user(request):
    login_form = LoginForm(request.POST or None)
    alert = None

    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            alert = 'Wrong username or password'

    return render_to_response(
        'login.html',
        {
            'login_form': login_form,
            'alert': alert,
        },
        context_instance=RequestContext(request),
    )


def logout_user(request):
    logout(request)
    return redirect('login_user')


@login_required
def home(request):
    task1 = {
        'title': 'Something very important',
        'author': 'John K',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed bibendum a dui vel accumsan. Sed vel purus et nunc vehicula ultrices.',
        'priority': 'normal',
        'end_date': '2016-01-27',
    }
    tasks = [task1, task1, task1, task1, task1]
    project1 = {
        'title': 'Test 1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed bibendum a dui vel accumsan. Sed vel purus et nunc vehicula ultrices.',
    }
    projects = [project1, project1, project1, project1, project1,]
    return render_to_response(
        'home.html',
        {
            'tasks': tasks,
            'projects': projects,
            'active_tab': 'home',
        },
        context_instance=RequestContext(request),
    )
