from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = 'shop'

    products = Product.objects.all()[:2]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    return render(request, 'stepshop/contact.html')


def about(request):
    return render(request, 'stepshop/about.html')
