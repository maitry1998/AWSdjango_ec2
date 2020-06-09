from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime
from AWSD.models import MembersModel,ActivityModel
from django.http import HttpResponse
from django.utils import timezone



class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ("start_time","end_time")



class MembersSerializer(serializers.ModelSerializer):
    Members_periods=ActivitySerializer(many=True)
    class Meta:
        model = MembersModel
        fields = ("ppid","real_name","tz","Members_periods")

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('Members_periods')
        question = MembersModel.objects.create(**validated_data)
        choice_set_serializer = self.fields['Members_periods']
        choices = choice_set_serializer.create(choice_validated_data)
        for a in choices:
            question.Members_periods.add(a)
        question.save()
        return question
