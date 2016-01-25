from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, render_to_response, RequestContext

from .forms import LoginForm


def login(request):
    login_form = LoginForm(request.POST or None)

    return render_to_response(
        'login.html',
        {
            'login_form': login_form,
        },
        context_instance=RequestContext(request),
    )


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {},
        context_instance=RequestContext(request),
    )
