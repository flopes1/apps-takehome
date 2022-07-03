from rest_framework import viewsets
from parts_api.api import serializers
from parts_api import models


class PartViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PartSerializer
    queryset = models.Part.objects.all()
