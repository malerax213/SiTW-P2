from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")

@when('I register crime')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('crime_create'))
        if context.browser.url == context.get_url('crime_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for crime')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from ukPolice.models import Crime
    crime = Crime.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(crime)

@then('There are {count:n} crimes')
def step_impl(context, count):
    from ukPolice.models import Crime
    assert count == Crime.objects.count()

@when('I edit the crime with category "{category}"')
def step_impl(context, category):
    from ukPolice.models import Crime
    crime = Crime.objects.get(category=category)
    context.browser.visit(context.get_url('crime_edit', crime.pk))
    if context.browser.url == context.get_url('crime_edit', crime.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for crime by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from ukPolice.models import Crime
    crime = Crime.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(crime)
