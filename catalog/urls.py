from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, Contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('about/<int:pk>', ProductDetailView.as_view(), name='about'),
]

