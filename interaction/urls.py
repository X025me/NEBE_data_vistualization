from django.urls import path, include
from . import views

urlpatterns = [
   path('request_list_aproved/', views.RequstViewSetYes.as_view(), name="approved"),
   path('request_list_notapproved/', views.RequstViewSetNot.as_view(),name="not approved"),
   #request
   path('request_change/<str:model>', views.request_create, name="request data change")


]