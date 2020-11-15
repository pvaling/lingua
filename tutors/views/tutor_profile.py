from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render

from tutors.forms.tutor_form import TutorProfileForm, AvatarForm
from tutors.models import Tutor

def tutor_profile(request):

    if request.method == 'GET':
        form = TutorProfileForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'about': request.user.tutor.about,
                'price': request.user.tutor.price,
                'is_available': request.user.tutor.is_available,
                'is_approved': request.user.tutor.is_approved,
                'experience_years': request.user.tutor.experience_years,
        })

    if request.POST:
        form = TutorProfileForm(request.POST,
                                initial={
                                    'first_name': request.user.first_name,
                                    'last_name': request.user.last_name,
                                    'is_approved': request.user.tutor.is_approved,
                                })
        if form.is_valid():

            request.user.tutor.about = form.cleaned_data['about']
            request.user.tutor.is_available = form.cleaned_data['is_available']
            # request.user.tutor.is_approved = form.
            request.user.tutor.price = form.cleaned_data['price']
            request.user.tutor.experience_years = form.cleaned_data['experience_years']

            request.user.save()


    context = {
        'form': form
    }



    return render(request, 'tutors/tutor_profile.html', context=context)
