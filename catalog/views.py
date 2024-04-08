from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    context = {'object_list': Product.objects.all(),
               }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, phone: {phone}, Message: {message}')

    return render(request, 'catalog/contacts.html')


def about(request, pk):
    context = {'object': Product.objects.get(pk=pk),
               }
    return render(request, 'catalog/about.html', context)
