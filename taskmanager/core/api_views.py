from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from .helper import get_epoch_timestamp
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
    """
    Create comment using Ajax call
    :param request:
    :param task_id:
    :return:
    """
    form = CommentForm(
        request.POST,
        task_id=task_id,
        user=request.user,
    )
    if form.is_valid():
        response_data = {
            'data': {
                'status': 'ok'
            }
        }
        return JsonResponse(
            data=response_data
        )
    else:
        response_data = {
            'data': {
                'errors': form.errors
            }
        }
        return JsonResponse(
            data=response_data,
        )


def comments_get(request, task_id):
    comments = Comment.objects.filter(
        task__id=task_id
    ).order_by('created_date')

    comments_data = []
    for comment in comments:
        comments_data.append({
            'id': comment.id,
            'author': comment.author.username,
            'is_author': True if comment.author == request.user else False,
            'text': comment.text,
            'created_date': get_epoch_timestamp(comment.created_date),
            'modified_date': get_epoch_timestamp(comment.modified_date),
        })

    response_data = {
        'data': {
            'comments': comments_data
        }
    }
    return JsonResponse(data=response_data)


