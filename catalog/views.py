from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from pytils.translit import slugify
from catalog.forms import ProductForm, BlogForm, VersionForm, ModeratorForm
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_categories


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['versions'] = Version.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:edit_catalog')

    def form_valid(self, form):
        if form.is_valid():
            product = form.save(commit=False)
            product.user = self.request.user
            product.save()
            return super().form_valid(form)
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:edit_catalog')

    def get_form_class(self):
        """
        Выводит форму в зависимости от прав пользователя и если модератор владелец продукта
        то выводит полную версию формы.
        """
        user = self.request.user
        if user.is_superuser:
            return ProductForm
        if user == self.object.user:
            return ProductForm
        if user.has_perm('catalog.change_cat_product') and user.has_perm(
                'catalog.publish_product') and user.has_perm(
            'catalog.describe_product') and user != self.object.user:
            return ModeratorForm

        raise PermissionDenied


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class Contacts(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, Message: {message}')
        return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        if self.object.slug == slugify(self.object.heading):
            return reverse('catalog:view', kwargs={'slug': self.object.slug})
        return reverse('catalog:view', args=[self.kwargs.get('slug')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def is_published_activity(request, slug):
    blog_item = get_object_or_404(Blog, slug=slug)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True

    blog_item.save()

    return redirect(reverse('catalog:blog_list', ))


def edit_published(request):
    context = {'object_list': Blog.objects.all(),
               }
    return render(request, 'catalog/published_activity.html', context)


def edit_catalog(request):
    context = {'object_list': Product.objects.all(),
               'versions': Version.objects.all(),
               }
    return render(request, 'catalog/edit_catalog.html', context)


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:edit_catalog')


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:edit_catalog')


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:edit_catalog')


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories()
