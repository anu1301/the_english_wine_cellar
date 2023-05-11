from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the wishlist """

    product = get_object_or_404(Product, pk=product_id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, 'Successfully added product to wishlist')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
