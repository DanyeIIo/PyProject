from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


def products(request, pk=0):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()
    products_all = Product.objects.all().order_by('price')

    context = {

        'title': title,
        'links_menu': links_menu,
        # 'links_category_menu': links_category_menu,
        'products_all': products_all,
    }

    if pk == 0:
        products_all = Product.objects.all().order_by('price')
        category = {'name': 'all'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_all = Product.objects.filter(category__pk=pk).order_by('price')

    context['category'] = category
    context['products_all'] = products_all

    return render(request=request, template_name='mainapp/products.html', context=context)


def product(request, pk):
    title = 'product'

    links_menu = ProductCategory.objects.all()

    current_products = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'links_menu': links_menu,
        'current_products': current_products,
    }

    return render(request=request, template_name='mainapp/product.html', context=context)
