from django.contrib import admin
from ukPolice.models import *

admin.site.register(Crime)
admin.site.register(Outcome)
admin.site.register(StreetLevelCrime)
admin.site.register(StreetLevelOutcome)
admin.site.register(Neighbourhood)
admin.site.register(NeighbourhoodPriority)
