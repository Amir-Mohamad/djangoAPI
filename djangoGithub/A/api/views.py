from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import GithubForm
from .scripts import get_data


def home(request):
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            context = {
                'data':get_data(form.cleaned_data['username'])
            }
            form.save()
    else:
        form = GithubForm()
    context = {
        'form':form
    }
    return render(request, 'api/home.html', context)