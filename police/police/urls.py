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
from ukPolice.views import main, signup, home, crimes, outcomes, neighbourhoodpriorities, CrimeDelete, OutcomeDelete, NeighbourhoodPriorityDelete
from django.views.generic.edit import CreateView
from ukPolice.forms import CrimeForm, OutcomeForm, NeighbourhoodPriorityForm
from ukPolice.models import Crime, Outcome, NeighbourhoodPriority
from ukPolice.views import LoginRequiredCheckIsOwnerUpdateView

from ukPolice.views import APICrimeList, APICrimeDetail, APIOutcomeList, APIOutcomeDetail, APINeighbourhoodPriorityList, APINeighbourhoodPriorityDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^signup$', signup, name='signup'),
    url(r'^login/', login, {'template_name': 'login.html', }, name='login'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^home/', home, name="home"),
    url(r'^crimes/', crimes, name="crimes"),
    url(r'^outcomes/', outcomes, name="outcomes"),
    url(r'^neighbourhoodpriorities/', neighbourhoodpriorities, name="neighbourhoodpriorities"),
	url(r'^registerCrime/$',  # Register Crime
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
    url(r'^crime/(?P<pk>\d+)/delete/$', CrimeDelete.as_view(), name="delete"),  # Delete a Crime
	url(r'^registerOutcome/$',  # Register Outcome
    	CreateView.as_view(
	       model=Outcome,
           template_name='form.html',
           form_class=OutcomeForm),
           name='outcome_create'),
    url(r'^outcome/(?P<pk>\d+)/$',  # View Outcome details
        DetailView.as_view(
        model=Outcome,
        template_name='outcome_detail.html'),
        name='outcome_detail'),
    url(r'^outcome/(?P<pk>\d+)/delete/$', OutcomeDelete.as_view(), name="delete"),  # Delete an Outcome
    url(r'^outcome/(?P<pk>\d+)/edit/$',  # Edit Outcome
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Outcome,
            form_class=OutcomeForm),
            name='outcome_edit'),
    url(r'^registerNeighbourhoodPriority/$',  # Register NeighbourhoodPriority
    	CreateView.as_view(
	       model=NeighbourhoodPriority,
           template_name='form.html',
           form_class=NeighbourhoodPriorityForm),
           name='neighbourhoodPriority_create'),
    url(r'^neighbourhoodPriority/(?P<pk>\d+)/$',  # View NeighbourhoodPriority details
        DetailView.as_view(
        model=NeighbourhoodPriority,
        template_name='neighbourhoodPriority_detail.html'),
        name='neighbourhoodPriority_detail'),
    url(r'^neighbourhoodPriority/(?P<pk>\d+)/edit/$',  # Edit neighbourhoodPriority
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=NeighbourhoodPriority,
            form_class=NeighbourhoodPriorityForm),
            name='neighbourhoodPriority_edit'),
    url(r'^neighbourhoodPriority/(?P<pk>\d+)/delete/$', NeighbourhoodPriorityDelete.as_view(), name="delete"),  # Delete a NeighbourhoodPriority
    url(r'^admin/', admin.site.urls),
    ]

# Restful API

urlpatterns += [
    url(r'^api/crimes/$', APICrimeList.as_view(), name='crime-list'),
    url(r'^api/crimes/(?P<pk>\d+)/$', APICrimeDetail.as_view(), name='crime-detail'),
    url(r'^api/outcomes/$', login_required(APIOutcomeList.as_view()), name='outcome-list'),
    url(r'^api/outcomes/(?P<pk>\d+)/$', APIOutcomeDetail.as_view(), name='outcome-detail'),
    url(r'^api/neighbourhoodpriorities/$', APINeighbourhoodPriorityList.as_view(), name='neighbourhoodpriority-list'),
    url(r'^api/neighbourhoodpriorities/(?P<pk>\d+)/$', APINeighbourhoodPriorityDetail.as_view(), name='neighbourhoodpriority-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns,  allowed=['api', 'json', 'xml'])
