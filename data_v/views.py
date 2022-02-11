from asyncio import constants
from unittest import result
from django.db.models import Q
from django.shortcuts import render
from rest_framework.permissions import  IsAuthenticated, AllowAny
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes, api_view
from django.views.generic import TemplateView


from .serializers import CandidateSerializer, HoprconstituencySerializer, HOPRMAXVoteSerializer, RcMAXVoteSerializer, PollingstationSerializer, RConstituencySerializer, PoliticalPartySerializer, RCResultsSerializer, HOPRResultsSerializer
from .models import Candidate, Hoprconstituency, NewvoteHoprmax, NewvoteRcmax, Pollingstation, Regionalconstituency, Politicatparty, NewvoteHoprgeneral, Region, NewvoteRcgeneral, NewvoteRcresult, NewvoteHopresult


catchall = TemplateView.as_view(template_name='index.html')


class CandidateViewSet(generics.ListAPIView):
    # queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['=constituencyid__constituencyid', '=gender', '=constituencyid__regionid__regionid', '=electionid__electionid', '=regionalconstituencyid__regionalconstituencyid', '=electionid__electionid', '=politicalpartyid']
    lookup_url_kwarg = 'disability'

    def get_queryset(self):
        param = self.kwargs.get('disability')
        if param == 1:
            candidate = Candidate.objects.filter(disability=True)
        elif param == 2:
            candidate = Candidate.objects.filter(disability=False)
        else:
            candidate = Candidate.objects.all()
        return candidate


class ConstituencyViewSet(generics.ListAPIView):
    queryset = Hoprconstituency.objects.all()
    serializer_class = HoprconstituencySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['=regionid__regionid']


class RegionalConstituencyViewSet(generics.ListAPIView):
    queryset = Regionalconstituency.objects.all()
    serializer_class = RConstituencySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['=regionid__regionid']

    
class RCResultsViewSet(generics.ListAPIView):
    serializer_class = RCResultsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['=general__region__regionid', '=general__rcconstituency__regionalconstituencyid', '=candidate__gender', '=party__politicalpartyid']


    def get_queryset(self):
        param = self.kwargs.get('disability')
        if param == 1:
            result = NewvoteRcresult.objects.filter(candidate__disability=True)
        elif param == 2:
            result = NewvoteRcresult.objects.filter(candidate__disability=False)
        else:
            result = NewvoteRcresult.objects.all()
        return result

class HOPRResultsViewSet(generics.ListAPIView):
    serializer_class = HOPRResultsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['=general__region__regionid', '=general__hoprconstituency__constituencyid', '=candidate__gender', '=party__politicalpartyid']


    def get_queryset(self):
        param = self.kwargs.get('disability')
        if param == 1:
            result = NewvoteHopresult.objects.filter(candidate__disability=True)
        elif param == 2:
            result = NewvoteHopresult.objects.filter(candidate__disability=False)
        else:
            result = NewvoteHopresult.objects.all()
        return result

class HOPRMAXVoteViewset(generics.ListAPIView):
    serializer_class = HOPRMAXVoteSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['=result__general__region__regionid', '=result__general__hoprconstituency__constituencyid', '=result__candidate__gender', '=result__candidate__politicalpartyid']
    lookup_url_kwarg = 'disability'

    def get_queryset(self):
        param = self.kwargs.get('disability')
        if param == 1:
            candidate = NewvoteHoprmax.objects.filter(result__candidate__disability=True)
        elif param == 2:
            candidate = NewvoteHoprmax.objects.filter(result__candidate__disability=False)
        else:
            candidate = NewvoteHoprmax.objects.all()
        return candidate

class RCMAXVoteViewset(generics.ListAPIView):
    serializer_class = RcMAXVoteSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['=result__general__region__regionid', '=result__general__rcconstituency__regionalconstituencyid', '=result__candidate__gender', '=result__party__politicalpartyid']
    lookup_url_kwarg = 'disability'

    def get_queryset(self):
        param = self.kwargs.get('disability')
        if param == 1:
            candidate = NewvoteRcmax.objects.filter(result__candidate__disability=True)
        elif param == 2:
            candidate = NewvoteRcmax.objects.filter(result__candidate__disability=False)
        else:
            candidate = NewvoteRcmax.objects.all()
        return candidate

class PollingStationViewset(generics.ListAPIView):
    queryset = Pollingstation.objects.all()
    serializer_class = PollingstationSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['=constituencyid__regionid__regionid', '=kebeleid__kebeleid', '=kebeleid__woredaid__woredaid', '=constituencyid__constituencyid', '=regionalconstituencyid__regionalconstituencyid']


class PoliticalpartyViewset(generics.ListAPIView):
    queryset = Politicatparty.objects.all()
    serializer_class = PoliticalPartySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)



#result anouncment code
@api_view(['GET'])
@permission_classes([AllowAny])
def hopr_details_region(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        response = []
        for region in regions:
            data = {
                'regionid': region.regionid,
                'region': region.regionname,
                'no_registerd_voters_hopr': 0,
                'no_registerd_voters_rc': 0,
                'no_votes_hopr': 0,
                'no_votes_rc': 0,
                'no_of_hopr_seat': 0,
                'no_of_rc_seat': 0,
                'no_of_sept20_rc': 0,
                'hopr_win_party': [
                    
                ],
                'rc_win_party': [],
                're_count_rc': 0,
                're_election_rc': 0


            }
            # number of registered voters
            rcs = NewvoteRcgeneral.objects.all().filter(Q(approve=True) & Q(region__regionid=region.regionid))
            hoprs = NewvoteHoprgeneral.objects.all().filter(Q(approved=True) & Q(region__regionid=region.regionid))
            
            for hopr in hoprs:
                data['no_registerd_voters_hopr'] = data['no_registerd_voters_hopr']+hopr.q1
                data['no_votes_hopr'] = data['no_votes_hopr']+hopr.q3
                data['no_of_hopr_seat'] = data['no_of_hopr_seat']+1
            for rc in rcs:
                data['no_registerd_voters_rc'] = data['no_registerd_voters_rc']+rc.q1
                data['no_votes_rc'] = data['no_votes_rc']+rc.q3
                data['no_of_rc_seat'] = data['no_of_rc_seat']+rc.no_of_seat

            # no of winning party and their seat number
            winner = []
            holder = []
            for hopr in hoprs:

                winners = NewvoteHoprmax.objects.get(result__general=hopr)
                
                if winners.result.party.politicalpartyname not in winner:
                    winner.append(winners.result.party.politicalpartyname)  # appending the winnner
                    detail = {
                        'name': winners.result.party.politicalpartyname,
                        'seat': 1
                    }
                    holder.append(detail)
                elif winners.result.party.politicalpartyname in winner:
                    for i in holder:
                        if i['name'] == winners.result.party.politicalpartyname:
                            i['seat'] = i['seat']+1
                
            for i in holder:
                data['hopr_win_party'].append(i)

            # no of winning party and their seat number for rc
            
            holderc = []
            for rc in rcs:
                
                winnersc = NewvoteRcmax.objects.filter(result__general=rc)
                for winnerr in winnersc: # looping over multiple rc winners
                    winnerc = []
                    if winnerr.result.party.politicalpartyname not in winnerc: # checking if the winner exists in winner list to avoid duplication
                        winnerc.append(winnerr.result.party.politicalpartyname)  # appending the winnner
                        detail = {
                            'name': winnerr.result.party.politicalpartyname,
                            'seat': 1
                        }
                        holderc.append(detail)
                    elif winnerr.result.party.politicalpartyname in winnerc:
                        for i in holderc:
                            if i['name'] == winnerr.result.party.politicalpartyname:
                                i['seat'] = i['seat']+1
            
            newHolder = []
            newWinner = []
            for i in holderc:
                if i['name'] not in newWinner:
                    newWinner.append(i['name'])
                    newHolder.append(i)
                elif i['name'] in newWinner:
                    for j in newHolder:
                        if j['name'] == i['name']:
                            j['seat'] = j['seat']+1
               
            for m in newHolder:
                data['rc_win_party'].append(m)
                        
                
                
                
            response.append(data)

        return Response(response)
            
        # hopr =  Hoprconstituency.objects.all().filter(regionid=id)