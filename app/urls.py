"""sprawdzarka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.controller import homepage, solution, test
from app.controller import algorithm

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage.index, name="homepage"),
    path('solution/add', solution.add, name="solution_add"),
    path('solution/list', solution.showAll, name="solution_list"),
    path('solution/details/<int:id>/', solution.details, name="solution_details"),
    path('test/add', test.add, name="test_add"),
    path('test/list', test.list, name='test_list'),
    path('algorithm/add', algorithm.add, name="algorithm_add"),
    path('algorithm/list', algorithm.list, name='algorithm_list'),
    # path('registration/login','django.contrib.auth.views.login'),
    path('registration/login',homepage.login_page,name='login'),

    path('registration/register', homepage.register_page,name='register'),
    path('registration/register_success', homepage.register_page,name='register_success'),

]
