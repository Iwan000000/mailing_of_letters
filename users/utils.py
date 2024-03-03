from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def send_email_for_verify(request, user):
    """
    Эта функция для отправки пользователю электронной почты со ссылкой для проверки.
    """
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'users/verify_email.html',
        context=context,
    )
    send_mail(
        subject='Veryfi email',
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
