from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewsLetterSub
from .forms import NewsLetterForm


def newsletter_sub(request):
    """ A view to handle the user newsletter subscription """
    form = NewsLetterForm()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetterSub.objects.filter(
                    email=instance.email).exists():
                messages.error(request, 'You have already signed up \
                    for a subscription')
            else:
                instance.save()
                messages.success(request, 'Thank you for signing up for a \
                    subscription to our newsletter')

                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'newsletter/newsletter.html', context)
   
