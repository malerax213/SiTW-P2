"""police URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib import admin
from django.contrib.auth.views import login, logout
from ukPolice.views import main, signup, home, crimes, outcomes, neighbourhoodpriorities
from django.views.generic.edit import CreateView
from ukPolice.forms import CrimeForm, OutcomeForm, NeighbourhoodPriorityForm
from ukPolice.models import Crime, Outcome, NeighbourhoodPriority
from ukPolice.views import LoginRequiredCheckIsOwnerUpdateView

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^signup$', signup, name='signup'),
    url(r'^login/', login, {'template_name': 'login.html', }, name='login'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^home/', home, name="home"),
    url(r'^crimes/', crimes, name="crimes"),
    url(r'^outcomes/', outcomes, name="outcomes"),
    url(r'^neighbourhoodpriorities/', neighbourhoodpriorities, name="neighbourhoodpriorities"),
	url(r'^registerCrime/$', # Register Crime
    	CreateView.as_view(
	       model=Crime,
           template_name='form.html',
           form_class=CrimeForm),
           name='crime_create'),
    url(r'^crime/(?P<pk>\d+)/$', # View crime details
        DetailView.as_view(
        model=Crime,
        template_name='crime_detail.html'),
        name='crime_detail'),
    url(r'^crime/(?P<pk>\d+)/edit/$', # Edit Crime
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Crime,
            form_class=CrimeForm),
            name='crime_edit'),
	url(r'^registerOutcome/$', # Register Outcome
    	CreateView.as_view(
	       model=Outcome,
           template_name='form.html',
           form_class=OutcomeForm),
           name='outcome_create'),
    url(r'^outcome/(?P<pk>\d+)/$', # View Outcome details
        DetailView.as_view(
        model=Outcome,
        template_name='outcome_detail.html'),
        name='outcome_detail'),
    url(r'^registerNeighbourhoodPriority/$', # Register NeighbourhoodPriority
    	CreateView.as_view(
	       model=NeighbourhoodPriority,
           template_name='form.html',
           form_class=NeighbourhoodPriorityForm),
           name='neighbourhoodPriority_create'),
    url(r'^neighbourhoodPriority/(?P<pk>\d+)/$', # View NeighbourhoodPriority details
        DetailView.as_view(
        model=NeighbourhoodPriority,
        template_name='neighbourhoodPriority_detail.html'),
        name='neighbourhoodPriority_detail'),
    url(r'^admin/', admin.site.urls),
]
