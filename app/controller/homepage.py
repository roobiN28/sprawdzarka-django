from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.template import RequestContext
from django.template.loader import get_template

from app.forms import LoginForm, RegisterForm


def index(request):
    return render(request, 'view/homepage.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            template = get_template("view/homepage.html")
            variables = RequestContext(request, {'user': user})
            output = template.render(variables)
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    template = get_template("view/registration/login.html")
    # variables = RequestContext(request, {'form': form})
    variables ={
        'request' : request,
        'form': form
    }
    return HttpResponse(template.render(variables))

def register_page(request):
    template = get_template('view/registration/register.html')
    form = RegisterForm()
    # variables = RequestContext(request,{'form':form})
    variables = {
        'request' : request,
        'form': form
    }
    # output = template.render(variables)
    return HttpResponse(template.render(variables))