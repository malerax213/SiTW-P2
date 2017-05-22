from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from forms import SignUpForm
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ukPolice.models import Outcome, NeighbourhoodPriority, Crime, Neighbourhood
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import CrimeForm, OutcomeForm, NeighbourhoodPriorityForm
from django.urls import reverse_lazy

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import CrimeSerializer, OutcomeSerializer, NeighbourhoodPrioritySerializer

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'

@login_required()
def home(request):
    return render_to_response('home.html', {
        'user': request.user
    })

def main(request):
    return render_to_response('main.html')

def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('signup.html', data)

def crimes(request):
    user = User.objects.get(username=request.user)
    crimes = user.crime_set.all()

    return render_to_response('crimes.html', {
        'username': request.user,
        'crimes': crimes
    })

def outcomes(request):
    outcomes = Outcome.objects.all()

    return render_to_response('outcomes.html', {
        'outcomes': outcomes
    })

def neighbourhoodpriorities(request):
    np = NeighbourhoodPriority.objects.all()

    return render_to_response('neighbourhoodpriorities.html', {
        'np': np
    })

from django.contrib.auth.decorators import login_required
class CrimeCreate(CreateView):
    model = Crime
    template_name = 'form.html'
    form_class = CrimeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrimeCreate, self).form_valid(form)

class OutcomeCreate(CreateView):
    model = Outcome
    template_name = 'form.html'
    form_class = OutcomeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OutcomeCreate, self).form_valid(form)

class NeighbourhoodPriorityCreate(CreateView):
    model = NeighbourhoodPriority
    template_name = 'form.html'
    form_class = NeighbourhoodPriorityForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NeighbourhoodPriorityCreate, self).form_valid(form)

class CrimeDelete(DeleteView):
    model = Crime
    template_name = 'crime_confirm_delete.html'

    def get_success_url(self):
        return reverse("crimes")

class OutcomeDelete(DeleteView):
    model = Outcome
    template_name = 'outcome_confirm_delete.html'

    def get_success_url(self):
        return reverse("outcomes")

class NeighbourhoodPriorityDelete(DeleteView):
    model = NeighbourhoodPriority
    template_name = 'neighbourhoodPriority_confirm_delete.html'

    def get_success_url(self):
        return reverse("neighbourhoodpriorities")

class APICrimeList(generics.ListCreateAPIView):
    model = Crime
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class APICrimeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Crime
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class APIOutcomeList(generics.ListCreateAPIView):
    model = Outcome
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class APIOutcomeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Outcome
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class APINeighbourhoodPriorityList(generics.ListCreateAPIView):
    model = NeighbourhoodPriority
    queryset = NeighbourhoodPriority.objects.all()
    serializer_class = NeighbourhoodPrioritySerializer

class APINeighbourhoodPriorityDetail(generics.RetrieveUpdateDestroyAPIView):
    model = NeighbourhoodPriority
    queryset = NeighbourhoodPriority.objects.all()
    serializer_class = NeighbourhoodPrioritySerializer
