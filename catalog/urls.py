from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    # path('contacts/', views.contacts, name='contacts'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/<int:pk>', views.ProductDetailView.as_view(), name='about'),
]

