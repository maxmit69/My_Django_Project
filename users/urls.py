from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, activate_user, UserResetPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<str:token>/', activate_user, name='activate'),
    path('password_reset/', UserResetPasswordView.as_view(template_name='users/password_reset.html', ),
         name='password_reset'),]
