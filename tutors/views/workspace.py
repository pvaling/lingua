from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from tutors.forms.tutor_form import TutorProfileForm
from tutors.forms.workspace_settings_form import WorkspaceSettingsForm
from tutors.models import User, JobRequest


def workspace_index(request):

    context = {
        'active_nav': 'workspace'
    }

    return render(request, 'tutors/workspace/workspace.html', context=context)

def workspace_settings(request):
    user: User = request.user

    if request.method == 'POST':
        f = WorkspaceSettingsForm(request.POST)
        if f.is_valid():
            user_type = f.cleaned_data.get('user_type')
            user.switch_type(user_type)

        return redirect(reverse('tutors:workspace_settings'))


    context = {
        'form': WorkspaceSettingsForm(initial={'user_type': user.get_user_type()}),
        'active_nav': 'workspace',
        'active_sidebar': 'settings',
    }

    return render(request, 'tutors/workspace/settings.html', context=context)

def workspace_tutor_profile_edit(request):

    if request.POST:
        form = TutorProfileForm(request.POST, request.FILES, instance=request.user.tutor)
        if form.is_valid():
            form.save()

        return redirect(reverse('tutors:workspace_tutor_profile_edit'))

    form = TutorProfileForm(instance=request.user.tutor)

    context = {
        'form': form,
        'active_nav': 'workspace',
        'active_sidebar': 'workspace_tutor_profile_edit',
    }

    return render(request, 'tutors/workspace/tutor_profile_edit.html', context=context)

#
# def workspace_orders_list(request):
#     context = {}
#     return render(request, 'tutors/workspace/orders_list.html', context=context)


class OrderList(ListView):
    model = JobRequest

    def get_queryset(self):
        return JobRequest.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['active_sidebar'] = 'orders'
        return context


class OrderDetailView(DetailView):
    model = JobRequest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrderDelete(DeleteView):
    model = JobRequest
    success_url = reverse_lazy('tutors:workspace_orders_list')
