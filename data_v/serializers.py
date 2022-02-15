from dataclasses import field, fields
from operator import mod
from pyexpat import model
from rest_framework import serializers
from .models import Candidate, Pollingstation, Politicatparty, NewvoteHoprmax, NewvoteRcmax, Hoprconstituency, Regionalconstituency, Region, NewvoteRcmax, NewvoteRcresult, NewvoteHopresult, NewvoteHoprgeneral, NewvoteRcgeneral


class PoliticalPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Politicatparty
        fields = ['politicalpartyid', 'politicalpartyname', 'politicalpartynameen', 'representative']

class CandidateSerializer(serializers.ModelSerializer):
    party = serializers.SerializerMethodField()
    constituency = serializers.SerializerMethodField()
    rcconstituency = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = ['fullname', 'candidateid', 'gender','constituencyid', 'regionalconstituencyid', 'electionid', 'politicalpartyid', 'disability', 'telephone', 'address', 'kebeleid', 'party', 'constituency', 'rcconstituency', 'region' ]


    def get_party(self, obj):
        party = Politicatparty.objects.get(politicalpartyid=obj.politicalpartyid)
        data = {}
        data['partyName'] = party.politicalpartyname
        return data['partyName']

    def get_constituency(self, obj):
        party = Hoprconstituency.objects.get(constituencyid=obj.constituencyid.constituencyid)
        data = {}
        data['constituency'] = party.constituencyname
        return data['constituency']

    def get_region(self, obj):
        party = Hoprconstituency.objects.get(constituencyid=obj.constituencyid.constituencyid)
        data = {}
        data['regionid'] = party.regionid.regionid
        region = Region.objects.get(regionid=int(data['regionid']))
        data['region'] = region.regionname
        return data['region']

    def get_rcconstituency(self, obj):
        if obj.regionalconstituencyid:
            party = Regionalconstituency.objects.get(regionalconstituencyid=obj.regionalconstituencyid.regionalconstituencyid)
            data = {}
            data['regionalconstituency'] = party.regionalconstituencyname
            return data['regionalconstituency']
        else: 
            return 0




class HoprconstituencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hoprconstituency
        fields=['constituencyid', 'constituencyname']


class RConstituencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Regionalconstituency
        fields = ['regionalconstituencyid', 'regionalconstituencyname']

        
# HOPR Maximum voted people
class HOPRMAXVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewvoteHoprmax
        fields = '__all__'
        depth=2


class RcMAXVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewvoteRcmax
        fields = '__all__'
        depth=3

class HOPRGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewvoteHoprgeneral
        fields = '__all__'
        depth=2

class RCGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewvoteRcgeneral
        fields = '__all__'
        depth=2

        
class PollingstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pollingstation
        fields = '__all__'


# result Serializer for RC and HOPR
class RCResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewvoteRcresult
        fields = '__all__'
        depth = 2

class HOPRResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewvoteHopresult
        fields = '__all__'
        depth = 2


class RequestViewSerializer(serializers.ModelSerializer):
    candiate = serializers.SerializerMethodField()
    constituency = serializers.SerializerMethodField()

    class Meta:
        model=NewvoteHoprmax
        fields =['id', 'candiate', 'constituency']
        depth: 3

    def get_candiate(self, obj):
        candidate = obj.result.candidate
        data ={
            'candidateName': candidate.fullname,
            'vote': obj.result.vote,
            
        }
        return data

    def get_constituency(self, obj):
        constituency = Hoprconstituency.objects.get(constituencyid=obj.result.candidate.constituencyid.constituencyid)
        data = {
            'name': constituency.constituencyname,
            'id': constituency.constituencyid
        }
        return data
