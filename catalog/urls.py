from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact, name='contact'),
    path('about/<int:pk>', views.about, name='about'),
]

