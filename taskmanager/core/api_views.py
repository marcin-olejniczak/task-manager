from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import CommentForm
from .models import Task, UserProfile, Comment


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


@require_http_methods(["POST"])
def comment_create(request, task_id):
    form = CommentForm(
        request.POST,
        task_id=task_id,
        user=request.user,
    )
    if form.is_valid():
        response_data = {
            'result': {
                'status': 'ok'
            }
        }
        return JsonResponse(
            data=response_data
        )
    else:
        response_data = {
            'result': {
                'errors': form.errors
            }
        }
        return JsonResponse(
            data=response_data,
        )


def task_comments(request, task_id):
    return JsonResponse(
        {
            'a': '1'
        }
    )

