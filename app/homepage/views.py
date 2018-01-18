from django.shortcuts import render


def index(request):
    param = request.GET.get('param')
    return render(request, 'homepage/index.html', {'title': param, 'body': 'BODY Test: ' + param}, request)
