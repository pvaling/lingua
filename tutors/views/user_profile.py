from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render

from tutors.models import Tutor, User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'cropping')


def user_profile(request):

    if request.method == 'GET':
        form = UserForm(instance=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'tutors/user_profile.html', context=context)
