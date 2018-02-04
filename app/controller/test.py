from django.shortcuts import render, redirect

from app.forms import TestForm
from app.models import Test


def add(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.save()
        return redirect('test_list')
    else:
        form = TestForm()
        return render(request, 'view/test/add.html', {'form': form})


def list(request):
    return render(request, 'view/test/list.html', {'model': Test.objects.all()})
