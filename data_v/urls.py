from django.urls import path, include
from . import views

urlpatterns = [
   path('candidate_list/<int:disability>', views.CandidateViewSet.as_view(), name="create hopr vote result"),
   path('hopr_max/<int:disability>/', views.HOPRMAXVoteViewset.as_view(), name="hopr winner list"),
   path('rc_max/<int:disability>/', views.RCMAXVoteViewset.as_view(), name="rc winner list"),
   path('constituency/', views.ConstituencyViewSet.as_view(), name="list of constituency"),
   path('rconstitunecy/', views.RegionalConstituencyViewSet.as_view(), name="regional constituency list"),
   path('pstation/', views.PollingStationViewset.as_view(), name="polling station list"),
   path('party_list/', views.PoliticalpartyViewset.as_view(), name="political party list"),
   #result anouncment 
   path('result_anouncement/', views.hopr_details_region, name="HOPR with region id"),
   # result For both rc and hopr
   path('result_rc/<int:disability>/', views.RCResultsViewSet.as_view(), name="regional constituency results"),
   path('result_hopr/<int:disability>/', views.HOPRResultsViewSet.as_view(), name="house of peoples representative election results")
]
