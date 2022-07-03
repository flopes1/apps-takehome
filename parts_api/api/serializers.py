from rest_framework import serializers
from parts_api import models


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Part
        fields = "__all__"
