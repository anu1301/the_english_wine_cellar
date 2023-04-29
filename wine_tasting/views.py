from django.shortcuts import render, get_object_or_404
from .models import Experiences
from .forms import BookingDate

# Create your views here.


def all_experiences(request):
    """ A view to show all experiences """

    experiences = Experiences.objects.all()

    context = {
        'experiences': experiences,
    }

    return render(request, 'experiences/experiences.html', context)


def experience_detail(request, experience_id):
    """ A view to show individual experience detail """

    form = BookingDate()

    experience = get_object_or_404(Experiences, pk=experience_id)

    context = {
        'experience': experience,
        "form": form,
    }

    return render(request, 'experiences/experience_detail.html', context)
