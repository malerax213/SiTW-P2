from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Crime, Outcome, NeighbourhoodPriority


class CrimeSerializer(HyperlinkedModelSerializer):
        uri = HyperlinkedIdentityField(view_name='crime-detail')
        user = CharField(read_only=True)

        class Meta:
                model = Crime
                fields = ('uri','category','persisten_id','latitude','longitude','date','user')

class OutcomeSerializer(HyperlinkedModelSerializer):
        uri = HyperlinkedIdentityField(view_name='outcome-detail')
        user = CharField(read_only=True)

        class Meta:
                model = Outcome
                fields = ('uri', 'code', 'name', 'user','Associated_crime')

class NeighbourhoodPrioritySerializer(HyperlinkedModelSerializer):
        uri = HyperlinkedIdentityField(view_name='neighbourhoodpriority-detail')
        neighbourhood = HyperlinkedRelatedField(view_name='neighbourhoodpriority-detail', read_only=True)
        user = CharField(read_only=True)

        class Meta:
            model = NeighbourhoodPriority
            fields = ('uri', 'action', 'user', 'action_date', 'issue', 'issue_date', 'neighbourhood')
