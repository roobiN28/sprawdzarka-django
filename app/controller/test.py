from django.shortcuts import render, redirect

from app.forms import TestForm
from app.models import Test, Algorithm


def add(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.save()
        return redirect('test_list')
    else:
        form = TestForm()
        return render(request, 'view/test/add.html', {'form': form, 'algorithms': Algorithm.objects.all()})


def list(request):
    return render(request, 'view/test/list.html', {'model': Test.objects.all()})
