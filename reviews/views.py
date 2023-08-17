from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import ReviewRating
from products.models import Product
from .forms import ReviewForm


def submit_review(request, product_id):
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id
                )
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Your review is being updated.')
            return HttpResponseRedirect(request.META["HTTP_REFERER"])

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request,
                    'Your feedback has successfully been submitted.'
                    )
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
