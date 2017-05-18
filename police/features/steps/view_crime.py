from behave import *

use_step_matcher("parse")

@when('I view the details for crime "{category}"')
def step_impl(context, crime_name):
    from ukPolice.models import Crime
    crime = Crime.objects.get(name=crime_name)
    context.browser.visit(context.get_url('crime_detail', crime.pk))

@then("I'm viewing restaurants details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
