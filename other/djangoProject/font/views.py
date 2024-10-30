from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormFromT, FormFromM
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        form = FormFromT()
        return render(request, 'index.html', context={'form' : form})
    else:
        form = FormFromT(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            return HttpResponse(f"{title}, {content}, {email}")
        else:
            return HttpResponse(form.errors)

@require_http_methods(['GET', 'POST'])
def mod(request):
    if request.method == 'GET':
        form = FormFromM()
        return render(request, 'model.html', context = {'form' : form})
    else:
        form = FormFromM(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('context')
            return HttpResponse(f"{title}, {content}")
        else:
            return HttpResponse(form.errors)