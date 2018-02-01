import random

from django.shortcuts import render
from django.template import RequestContext

from app.models import Test


def add(request):
    # context = RequestContext(request)
    if request.method == "POST":
        t = Test()
        # tutaj trzeba własnie wycignac dane z formuarza--------
        t.test_name = 'dodaj'
        t.input_data = 'input_data'
        t.output_data = 'output_data'
        # --------- sam zapis do bazy działa poprawnie
        t.save()
        return render(request,'view/test/added.html', {'test': t})

    else:
        return render(request, 'view/test/add.html')


# def createTest():
#     t = Test()
#     t.id = random.randint(0, 100)
#     t.input_data = 'input data'
#     t.output_data = 'output data'
