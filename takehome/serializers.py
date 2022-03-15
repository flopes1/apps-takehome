from rest_framework import serializers
from takehome.models import Widget


class WidgetSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = "__all__"
