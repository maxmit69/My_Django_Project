from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from pytils.translit import slugify
from catalog.forms import ProductForm, BlogForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['versions'] = Version.objects.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:edit_catalog')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:edit_catalog')


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
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


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
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


class BlogDeleteView(DeleteView):
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


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:edit_catalog')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:edit_catalog')


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:edit_catalog')
