from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
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
            # variables = RequestContext(request, {'user': user})
            # output = template.render(variables)
            return render(request, 'view/homepage.html', {'user': user})
            # return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    template = get_template("view/homepage.html")
    # variables = RequestContext(request, {'form': form})
    variables ={
        'request' : request,
        'form': form
    }
    return render(request, 'view/registration/login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            user.last_name = form.cleaned_data['phone']
            user.save()
            if form.cleaned_data['log_on']:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                login(request,user)
                return render(request, 'view/homepage.html',{'user':user})
            else:
                return render(request, 'view/registration/register_success.html',{'username':form.cleaned_data['username']})
    else:
        form = RegisterForm()
    return render(request, 'view/registration/register.html',{ 'form': form})



