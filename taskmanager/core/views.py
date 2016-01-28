from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import (
    redirect, render_to_response, RequestContext,
)
from .forms import LoginForm
from .models import *


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
    """
    Home view, displays dashboard with some basic info about tasks,
    projects and user activities.
    :param request:
    :return:
    """
    user = User.objects.filter(pk=request.user.id)

    tasks = Task.objects.filter(
        assignee__user=user,
    ).order_by(
        '-end_date'
    )[:5]

    projects = Project.objects.filter(
        members__user=user,
    ).order_by(
        '-end_date',
    )[:5]

    return render_to_response(
        'home.html',
        {
            'tasks': tasks,
            'projects': projects,
            'active_tab': 'home',
        },
        context_instance=RequestContext(request),
    )
