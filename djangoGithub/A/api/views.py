from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import GithubForm
from .scripts import get_data


def home(request):
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            form.save()
            return redirect('api:result', username)
    else:
        form = GithubForm()
    context = {
        'form':form
    }
    return render(request, 'api/home.html', context)

def result(request, username):
    data = get_data(username)
    return render(request, 'api/result.html', {'data':data})