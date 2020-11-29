from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from tutors.forms.tutor_form import TutorProfileForm, AvatarForm, TutorGalleryForm
from tutors.models import Tutor, GalleryItem


def tutor_profile_gallery(request):

    form = TutorGalleryForm(request.POST, request.FILES)

    if request.method == 'POST':
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for file in files:
                GalleryItem.objects.create(
                    tutor=request.user.tutor,
                    image=file,
                    order=1
                )

        if request.POST.get('action') == 'delete':
            item = GalleryItem.objects.get(tutor_id=request.user.tutor, id=int(request.POST.get('id')))
            item.delete()

        return HttpResponseRedirect(reverse("tutors:tutor_profile_gallery"))

    context = {
        'form': form,
        'gallery_items': GalleryItem.objects.filter(tutor=request.user.tutor)
    }

    return render(request, 'tutors/tutor_profile_gallery.html', context=context)
