from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import GithubForm
from .scripts import get_data


def home(request):
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            context = {
                'form':form,
                'data':get_data()
            }
            form.save()

    else:
        form = GithubForm()
        context = {
            'form':form
        }
    return render(request, 'api/home.html', context)