from django.shortcuts import render

def workspace_index(request):

    context = {
        'active_nav': 'workspace'
    }

    return render(request, 'tutors/workspace.html', context=context)
