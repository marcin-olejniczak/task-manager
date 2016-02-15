from django import forms
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit

from .models import Comment, Task


class LoginForm(forms.Form):
    """
    Login form
    """

    username = forms.CharField(
        label="Username",
        max_length=30,
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-signin'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('username', placeholder='Username'),
            Field('password', placeholder='Password'),
        )
        self.helper.add_input(Submit('submit', 'Sign In'))
        self.helper.form_action = '/login/'


class CommentForm(forms.ModelForm):
    """
    Comment Form
    """
    def __init__(self,  *args, **kwargs):
        self.helper = FormHelper()
        self.task_id = kwargs.pop('task_id', None)
        self.user = kwargs.pop('user', None)

        if self.task_id is not None:
            self.helper.form_action = reverse(
                'comment_create',
                kwargs={'task_id': self.task_id}
            )
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        text = cleaned_data.get('text', None)

        if text is not None:
            task = Task.objects.get(pk=self.task_id)
            comment = Comment(
                author=self.user,
                task=task,
                text=self.cleaned_data['text'],
            )
            comment.save()
        """
                        raise forms.ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )
        """

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5})
        }
        labels = {
            'text': 'Comment'
        }
