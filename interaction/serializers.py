from dataclasses import field
from datetime import date

from rest_framework import serializers
from .models import Request
from api.user.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils.module_loading import import_string
from data_v.models import NewvoteRcmax, NewvoteHoprmax, NewvoteHopresult, NewvoteHoprgeneral, NewvoteRcgeneral, NewvoteRcresult
from data_v.serializers import HOPRResultsSerializer, RcMAXVoteSerializer, HOPRMAXVoteSerializer, HOPRGeneralSerializer, NewvoteHopresult, RCGeneralSerializer, RCResultsSerializer
from generic_relations.relations import GenericRelatedField




class RequestCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = ['request_description', 'object_id' ]

    def create(self, validated_data):
        owner = self.context['request'].user
        print(self.context['request'].data['content_type'])
        object = ContentType.objects.get(model=self.context['request'].data['content_type'])
        print(object)
        request = Request.objects.create(owner=owner, content_type=object, **validated_data)
        return request
    
        

class ReqeuestedSerializer(serializers.Serializer):
    content_object = GenericRelatedField({
        NewvoteHoprmax: HOPRMAXVoteSerializer(),
        NewvoteRcmax: RcMAXVoteSerializer(),
        NewvoteRcresult: RCResultsSerializer(),
        NewvoteHopresult: HOPRResultsSerializer(),
        NewvoteRcgeneral: RCGeneralSerializer(),
        NewvoteRcgeneral: RCGeneralSerializer(),
    })
    # class Meta:
    #     fields = ['content_object']


class RequestSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    content_object = GenericRelatedField({
        NewvoteHoprmax: HOPRMAXVoteSerializer(),
        NewvoteRcmax: RcMAXVoteSerializer(),
        NewvoteRcresult: RCResultsSerializer(),
        NewvoteHopresult: HOPRResultsSerializer(),
        NewvoteRcgeneral: RCGeneralSerializer(),
        NewvoteHoprgeneral: HOPRGeneralSerializer(),


    })
    models = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['id', 'owner', 'status', 'request_description','content_type','object_id', 'content_object', 'created_date', "models"  ]


    def get_owner(self, obj):
        user = User.objects.get(id=obj.owner.id)
        return user.email
    
    def get_models(self, obj):
        type = obj.content_type.model_class()
        name =  type._meta.object_name
        data ={
            "name": name
        }
        return data


    
