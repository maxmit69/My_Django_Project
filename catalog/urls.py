from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('create/', views.ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/<int:pk>', views.ProductDetailView.as_view(), name='about'),
    path('edit_catalog/', views.edit_catalog, name='edit_catalog'),

    path('create/new/', views.BlogCreateView.as_view(), name='create'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('view/<slug:slug>', views.BlogDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/update/', views.BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='delete'),
    path('activity/<slug:slug>', views.is_published_activity, name='is_published_activity'),
    path('edit_blog/', views.edit_published, name='published_activity'),
]

