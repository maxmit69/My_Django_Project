from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View

from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/product_list.html'
    # template_name = 'catalog/index.html'


# def index(request):
#     context = {'object_list': Product.objects.all(),
#                }
#     return render(request, 'catalog/index.html', context)


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
        # return JsonResponse({'name': name, 'phone': phone, 'message': message})
        return render(request, 'catalog/contacts.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Name: {name}, phone: {phone}, Message: {message}')
#
#     return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'catalog/product_detail.html'
    template_name = 'catalog/about.html'

# def about(request, pk):
#     context = {'object': Product.objects.get(pk=pk),
#                }
#     return render(request, 'catalog/about.html', context)
