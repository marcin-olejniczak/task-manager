from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.shortcuts import (
    redirect, render_to_response, RequestContext,
)
from django.views.generic.edit import CreateView, UpdateView
from .forms import LoginForm
from .models import Comment, Task, User, Project


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
    ).order_by('-end_date')[:5]

    projects = Project.objects.filter(
        members__user=user,
    ).order_by('-end_date')[:5]

    return render_to_response(
        'home.html',
        {
            'tasks': tasks,
            'projects': projects,
            'active_tab': 'home',
        },
        context_instance=RequestContext(request),
    )


def project_edit(request, id=None):
    """
    View allows user to create or edit project
    :param request:
    :return:
    """
    project_form = {}

    return render_to_response(
        'project_edit.html',
        {
            'form': project_form,
            'active_tab': 'project',
        },
        context_instance=RequestContext(request),
    )


def project(request, id=None):
    """
    View allows user to see details about project
    :param request:
    :param id:
    :return:
    """
    project = {
        'id': id,
    }

    return render_to_response(
        'project.html',
        {
            'project': project,
            'active_tab': 'project',
        },
        context_instance=RequestContext(request),
    )


def task(request, id=None):
    """
    View allows user to see details about project
    :param request:
    :param id:
    :return:
    """
    task = {
        'id': id,
    }

    return render_to_response(
        'task.html',
        {
            'task': task,
            'active_tab': 'task',
        },
        context_instance=RequestContext(request),
    )


class BaseFormView(object):
    template_name = 'core/common_form.html'
    context_variables = {}

    def get_context_data(self, **kwargs):
        context = super(BaseFormView, self).get_context_data(**kwargs)
        context.update(self.context_variables)
        return context

    def dispatch(self, *args, **kwargs):
        return super(BaseFormView, self).dispatch(*args, **kwargs)


class TaskGenericView(BaseFormView):
    model = Task
    fields = [
        'title', 'description',
        'start_date', 'end_date', 'author',
        'assignee', 'project', 'priority',
        'status',
    ]


class TaskUpdate(TaskGenericView, UpdateView):
    context_variables = {
        'header': 'Update Task'
    }


class TaskCreate(TaskGenericView, CreateView):
    context_variables = {
        'header': 'Create Task'
    }


class ProjectGenericView(BaseFormView):
    model = Project
    fields = [
        'title', 'description', 'end_date',
        'start_date',
    ]


class ProjectUpdate(ProjectGenericView, UpdateView):
    context_variables = {
        'header': 'Update Project'
    }


class ProjectCreate(ProjectGenericView, CreateView):
    context_variables = {
        'header': 'Create Project'
    }
