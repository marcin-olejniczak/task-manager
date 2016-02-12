from django.http import HttpResponse, HttpResponseBadRequest

from .models import Task, UserProfile


def task_toggle_tracking(request, pk):
    """
    Allows to toggle tracking task
    :param request:
    :param pk:
    :return:
    """
    task = Task.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=request.user)

    if task:
        if user_profile.tracked_tasks.filter(id=pk).exists():
            user_profile.tracked_tasks.remove(task)
        else:
            user_profile.tracked_tasks.add(task)
    else:
        return HttpResponseBadRequest()

    return HttpResponse()
