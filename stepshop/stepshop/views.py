from django.shortcuts import render
from mainapp.models import Product

from basketapp.models import Basket


def get_basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return basket


def index(request):
    title = 'магазин'

    basket = get_basket(request)

    products = Product.objects.all()  # [:4]

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    title = 'contacts'

    basket = get_basket(request)

    context = {
        'title': title,
        'basket': basket
    }
    return render(request, 'stepshop/contact.html', context=context)


def about(request):
    title = 'about'

    basket = get_basket(request)

    context = {
        'title': title,
        'basket': basket
    }

    return render(request, 'stepshop/about.html', context=context)
