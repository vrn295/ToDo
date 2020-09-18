from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *


def index(request):
    tasks = Base.objects.all()
    form = BaseForm()

    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'base/home.html', context)
