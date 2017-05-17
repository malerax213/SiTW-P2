from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")

@given('Exists crime registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from ukPolice.models import Crime
    for row in context.table:
        crime = crime(user=user)
        for heading in row.headings:
            setattr(crime, heading, row[heading])
        crime.save()

@when('I register crime')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('ukPolice:crime_create'))
        if context.browser.url == context.get_url('ukPolice:crime_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} crime')
def step_impl(context, count):
    from ukPolice.models import Crime
    assert count == Crime.objects.count()
