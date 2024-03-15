from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User
from users.utils import send_email_for_verify


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AuthenticationForm(DjangoAuthenticationForm):
    """
    Форма для аутентификации пользователя.
    """

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=email,
                password=password,
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()

            else:
                if not self.user_cache.email_verify:  # checking verification
                    send_email_for_verify(self.request, self.user_cache)
                    raise ValidationError(
                        'Электронная почта не подтверждена, проверьте свою электронную почту',
                        code='Неверный логин',
                    )
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(UserChangeForm):
    """
    Форма добавления информации о пользователе
    """

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'lastname', 'company', 'phone', 'birthday', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['password'].widget = forms.HiddenInput()
