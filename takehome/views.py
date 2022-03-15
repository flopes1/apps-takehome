from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
import json
import sqlite3
from takehome.models import Widget
from takehome.serializers import WidgetSeralizer
from rest_framework.viewsets import ReadOnlyModelViewSet


def home(request):
    return render(request, 'index.html')

connection = sqlite3.connect("db.sqlite3")

def update_part(request, part_id):
    part = json.loads(request.body)
    # this table is part of the ERP application, so I can't create a model for it, because it tries to create migrations
    value_pairs = ",".join(("{key}='{value}'".format(key=key, value=value) if isinstance(value, (str, bool)) else '{key}={value}'.format(key=key, value=value) for key, value in part.items()))
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE parts SET {value_pairs} WHERE id={part_id}".format(value_pairs=value_pairs, part_id=part_id)
            )
    except:
        return HttpResponseServerError("Problem updating parts")

    return HttpResponse(status=200)


class WidgetViewSet(ReadOnlyModelViewSet):
    queryset = Widget.objects.order_by("name")
    serializer_class = WidgetSeralizer