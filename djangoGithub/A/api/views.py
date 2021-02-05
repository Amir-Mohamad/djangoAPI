from django.shortcuts import render
from django.views import View
from .forms import GithubForm
from .scripts import get_data

class Home(View):
    template_name = "api/home.html"
    form_class = GithubForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'data':get_data(form.cleaned_data['username'])
            }
        return render(request, self.template_name, {'form':form})