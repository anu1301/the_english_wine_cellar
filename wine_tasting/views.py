from django.shortcuts import render
from .models import Experiences

# Create your views here.


def all_experiences(request):
    """ A view to show all experiences """

    experiences = Experiences.objects.all()

    context = {
        'experiences': experiences,
    }

    return render(request, 'experiences/experiences.html', context)



