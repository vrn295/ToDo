from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

from rest_framework import viewsets
from rest_framework import permissions

from .seralizers import BaseSerializer


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


def update(request, pk):
    task = Base.objects.get(id=pk)
    form = BaseForm(instance=task)

    if request.method == "POST":
        form = BaseForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'base/update.html', context)


def delete(request, pk):
    item = Base.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'base/delete.html', context)


'''Serializers'''


class BaseViewSet(viewsets.ModelViewSet):
    queryset = Base.objects.all().order_by('-date_created')
    serializer_class = BaseSerializer
    permission_classes = [permissions.IsAuthenticated]
