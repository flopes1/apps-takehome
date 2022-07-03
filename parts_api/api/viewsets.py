from rest_framework import viewsets
from rest_framework.decorators import action
from parts_api.api import serializers
from parts_api import models
from django.http import HttpResponse

import nltk
import json

nltk.download("punkt")


class PartViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PartSerializer
    queryset = models.Part.objects.all()

    @action(detail=False, methods=['get'])
    def common_description(self, request, pk=None):
        """
        Returns the 5 most common words in the parts description
        """
        parts_description = self.queryset.values_list('description', flat=True)
        frequency_distribution = nltk.FreqDist(nltk.word_tokenize((" ".join(parts_description))))
        common_words = frequency_distribution.most_common(5)

        return HttpResponse(content=json.dumps(dict(common_words)))
