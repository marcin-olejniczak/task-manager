from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit


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
