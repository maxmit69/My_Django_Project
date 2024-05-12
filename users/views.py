from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
import django.views.generic
import secrets
from django.urls import reverse
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class RegisterView(django.views.generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        url = f'http://{host}/users/activate/{token}/'
        send_mail(
            subject='Активация аккаунта',
            message=f'Для активации аккаунта перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        user.save()
        message = 'Аккаунт успешно создан. Пожалуйста, подтвердите активацию через ссылку в письме.'
        return HttpResponse(message)


def activate_user(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy('users:login'))


class ProfileView(django.views.generic.UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserResetPasswordView(PasswordResetView):

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST.get('email')
            user = User.objects.filter(email=user_email).first()

            if user:
                new_password = BaseUserManager().make_random_password(20)
                user.set_password(new_password)
                user.save()
                try:
                    send_mail(
                        subject='Восстановление пароля',
                        message=f'Ваш новый пароль: {new_password}',
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email],
                    )
                except Exception:  # noqa
                    print(f'Ошибка при отправке письма на {user.email}')

        return HttpResponseRedirect(reverse('users:login'))
