from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
        
    
    products = Product.objects.all().order_by('-id')   
    return render(request, 'products/pages/home.html', context={
        'form': form, 'products': products
    })
    
    
def registred_products(request):
    products = Product.objects.all().order_by('id')
    return render(request,'products/pages/registred_products.html', context={
      'products': products,  
    })
    
    
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:registred_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/pages/edit_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products:registred_products')

    return render(request, 'products/pages/delete_product.html', {'product': product})
