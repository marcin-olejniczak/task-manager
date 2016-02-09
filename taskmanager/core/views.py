from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.shortcuts import (
    redirect, render_to_response, RequestContext,
)
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from .forms import LoginForm
from .models import Comment, Task, User, Project, ProjectMember


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

    def __init__(self, *args, **kwargs):
        if hasattr(self, 'global_variables'):
            self.global_context_variables.update(self.context_variables)
        else:
            self.global_context_variables = self.context_variables

        super(BaseFormView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseFormView, self).get_context_data(**kwargs)
        context.update(self.global_context_variables)
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


class TaskUpdateView(TaskGenericView, UpdateView):
    context_variables = {
        'form_title': 'Update Task'
    }


class TaskCreateView(TaskGenericView, CreateView):
    context_variables = {
        'form_title': 'Create Task'
    }


class TaskPreviewView(TaskGenericView, DetailView):
    context_object_name = 'task_object'
    template_name = 'core/task_project_preview.html'


class ProjectGenericView(BaseFormView):
    model = Project
    fields = [
        'title', 'description', 'end_date',
        'start_date', 'members'
    ]
    context_variables = {}

    def dispatch(self, *args, **kwargs):
        id = kwargs['pk']
        project_members = ProjectMember.objects.filter(
            project__id=id,
        ).filter(
            is_author=True,
        )
        authors = [mem.user for mem in project_members]
        self.context_variables.update({
            'project_authors': authors,
        })

        return super(ProjectGenericView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        project_obj = form.save(commit=False)
        form_members = list(form.cleaned_data['members'])
        authors = [self.request.user.id]
        if self.request.user not in form_members:
            form_members.append(self.request.user)

        for member in form_members:
            ProjectMember.objects.update_or_create(
                project=project_obj,
                user=member,
                is_author=True if member.id in authors else False,
            )
        ProjectMember.objects.filter(
            project=project_obj,
        ).exclude(
            user__in=form_members,
        ).delete()

        return super(ModelFormMixin, self).form_valid(form)


class ProjectUpdateView(ProjectGenericView, UpdateView):
    context_variables = {
        'form_title': 'Update Project'
    }


class ProjectCreateView(ProjectGenericView, CreateView):
    context_variables = {
        'form_title': 'Create Project'
    }


class ProjectPreviewView(ProjectGenericView, DetailView):
    context_object_name = 'project_object'
    template_name = 'core/task_project_preview.html'

