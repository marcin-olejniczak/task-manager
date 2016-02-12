from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.shortcuts import (
    redirect, render_to_response, RequestContext,
)
from django.http import HttpResponseForbidden
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView

from .forms import LoginForm
from .models import Comment, Task, User, Project, ProjectMember, UserProfile


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
        project_member__user=user,
        project_member__is_author=True,
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


def projects(request, id=None):

    projects_member = Project.objects.filter(
        project_member__user=request.user,
        project_member__is_author=False,
    )

    projects_author = Project.objects.filter(
        project_member__user=request.user,
        project_member__is_author=True,
    )

    return render_to_response(
        'projects.html',
        {
            'projects_member': projects_member,
            'projects_author': projects_author,
            'active_tab': 'projects',
        },
        context_instance=RequestContext(request),
    )


def tasks(request, id=None):
    assigned_tasks = Task.objects.filter(
        assignee=request.user
    )
    created_tasks = Task.objects.filter(
        author=request.user
    )
    tracked_tasks = Task.objects.filter(
        tracked_tasks__user=request.user
    )
    return render_to_response(
        'tasks.html',
        {
            'assigned_tasks': assigned_tasks,
            'created_tasks': created_tasks,
            'tracked_tasks': tracked_tasks,
            'active_tab': 'tasks',
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

        super(BaseFormView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseFormView, self).get_context_data(**kwargs)
        context.update(self.global_context_variables)
        return context

    def dispatch(self, *args, **kwargs):
        return super(BaseFormView, self).dispatch(*args, **kwargs)


class TaskGenericView(BaseFormView):
    model = Task
    fields = [
        'title', 'description', 'start_date', 'end_date', 'assignee',
        'project', 'priority', 'status',
    ]


class TaskUpdateView(TaskGenericView, UpdateView):
    context_variables = {
        'form_title': 'Update Task'
    }


class TaskCreateView(TaskGenericView, CreateView):
    context_variables = {
        'form_title': 'Create Task'
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super(ModelFormMixin, self).form_valid(form)


class TaskPreviewView(TaskGenericView, DetailView):
    context_object_name = 'task_object'
    template_name = 'core/task_project_preview.html'
    fields = [
        'title', 'description', 'start_date', 'end_date', 'assignee',
        'project', 'priority', 'status', 'author'
    ]

    def get_context_data(self, **kwargs):
        tracked_tasks = Task.objects.filter(
            tracked_tasks__user=self.request.user,
        )
        context = super(TaskPreviewView, self).get_context_data(**kwargs)
        context.update(
            {
                'tracked': self.object in tracked_tasks,
            }
        )

        return context

    def __init__(self, *args, **kwargs):
        super(TaskGenericView, self).__init__(self, *args, **kwargs)


class ProjectGenericView(BaseFormView):
    model = Project
    fields = [
        'title', 'description', 'end_date',
        'start_date', 'members'
    ]
    context_variables = {}

    def dispatch(self, *args, **kwargs):
        project_id = kwargs.get('pk')

        if project_id:
            project_members = ProjectMember.objects.filter(
                project__id=project_id,
            ).order_by('-is_author')

            authors = project_members.filter(
                is_author=True,
            )

            self.context_variables.update({
                'project_members': project_members,
                'project_authors': authors,
            })

        return super(ProjectGenericView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form_members = list(form.cleaned_data['members'])
        del form.cleaned_data['members']
        self.object = form.save()
        authors = [self.request.user.id]
        if self.request.user not in form_members:
            form_members.append(self.request.user)

        ProjectMember.objects.filter(
            project=self.object,
        ).exclude(
            user__in=form_members,
        ).delete()

        for member in form_members:
            ProjectMember.objects.update_or_create(
                project=self.object,
                user=member,
                is_author=True if member.id in authors else False,
            )

        return super(ModelFormMixin, self).form_valid(form)


class ProjectUpdateView(ProjectGenericView, UpdateView):
    context_variables = {
        'form_title': 'Update Project'
    }
    # TODO: only members who are managers can edit


class ProjectCreateView(ProjectGenericView, CreateView):
    context_variables = {
        'form_title': 'Create Project'
    }


class ProjectPreviewView(ProjectGenericView, DetailView):
    context_object_name = 'project_object'
    template_name = 'core/task_project_preview.html'

