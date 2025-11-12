from django.shortcuts import render

from mitienda.models import Producto, Categoria

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Categoria.objects.all()
    products=Producto.objects.all(available=True) 

    if category_slug:
        category= get.object_or_404(Categoria, slug=category_slug)
        products=products.filter(category=category)
    
    return render(request, 'tienda/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request,id,slug):
    product=get.object_or_404(Producto, id=id, slug=slug, available=True)
    return render(request,'tienda/product/detail.html', {'product': product})
