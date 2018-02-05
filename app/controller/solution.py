from django.shortcuts import render

from app.forms import SolutionForm
from app.logic.TestService import TestService
from app.models import Solution

import pdb

def add(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        solution = form.save()

        TestService(solution).doTest()
        return render(request, 'view/solution/added.html', {'solution': solution})
    else:
        form = SolutionForm()
        return render(request, 'view/solution/add.html', {'form': form})


def showAll(request):
    solutions = Solution.objects.all()
    return render(request, 'view/solution/solutions.html', {"solutions": solutions})


def details(request, id):
    solution = Solution.objects.get(id=id)
    return render(request, 'view/solution/solution.html', {'solution': solution})
