from django.shortcuts import render, get_object_or_404
from .models import Product
import urllib.request, json 

##
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    inputurl = "http://195.248.241.84:8888/api/recommend/thirdParty/?format=json&id={}".format(id)
    with urllib.request.urlopen(inputurl) as url:
        data = json.loads(url.read().decode())
    products = Product.objects.filter(id__in=data['recommendations'])
    context = {'products':products, 'product':product}
    return render(request, 'product/product_detail.html', context)

def store(request):
    products = Product.objects.order_by('-created')
    context = {'products':products}
    return render(request,'product/store.html', context)