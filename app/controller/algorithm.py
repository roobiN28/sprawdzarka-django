from django.shortcuts import render, redirect

from app.forms import AlgorithmForm
from app.models import Algorithm


def add(request):
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        form.save()
        return redirect('algorithm_list')
    else:
        form = AlgorithmForm()
        return render(request, 'view/algorithm/add.html', {'form': form})


def list(request):
    return render(request, 'view/algorithm/list.html', {'model': Algorithm.objects.all()})
