from rest_framework import viewsets
from . import serializers
from . import models


class MembersViewsets(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = models.MembersModel.objects.all()
    serializer_class = serializers.MembersSerializer


class ActivityViewsets(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = models.ActivityModel.objects.all()
    serializer_class = serializers.ActivitySerializer
