from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Crime(models.Model):
    category = models.TextField(max_length=20)
    persisten_id = models.TextField(max_length=60, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date = models.DateField(default=date.today)
    policeman_assignated = models.ForeignKey(User, default='')

    def __unicode__(self):
        return str(self.category)+"."+str(self.date)

    def get_absolute_url(self):
        return reverse('crime_detail', kwargs={'pk': self.pk})

class Outcome(models.Model):
    code = models.TextField(max_length=30)
    name = models.TextField(max_length=30)
    Associated_crime = models.ForeignKey(Crime)

    def __unicode__(self):
        return self.name+"."+str(self.code)

    def get_absolute_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.pk})

class StreetLevelCrime(models.Model):
    crime = models.ForeignKey(Crime)
    street_id = models.TextField(max_length=50)
    street_name = models.TextField(max_length=50)

    def __unicode__(self):
        return str(self.crime)+"."+str(self.street_name)

class StreetLevelOutcome(models.Model):
    outcome = models.ForeignKey(Outcome)
    street_id = models.TextField(max_length=50)
    street_name = models.TextField(max_length=50)

    def __unicode__(self):
        return str(self.outcome)+"."+str(self.street_name)

class Neighbourhood(models.Model):
    n_id = models.TextField(max_length=40)
    n_name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.n_id+"."+self.n_name

class NeighbourhoodPriority(models.Model):
    action = models.TextField(max_length=400,blank=True,null=True)
    action_date = models.DateField(default=date.today,blank=True,null=True)
    issue = models.TextField(max_length=400)
    issue_date = models.DateField(default=date.today)
    neighbourhood = models.ForeignKey(Neighbourhood)

    def __unicode__(self):
        return str(self.neighbourhood)+"."+str(self.issue_date)

    def get_absolute_url(self):
        return reverse('neighbourhoodPriority_detail', kwargs={'pkr': self.pk})
