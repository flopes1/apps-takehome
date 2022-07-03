from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render
from contextlib import closing

import json

from rest_framework.viewsets import ReadOnlyModelViewSet

# Updated to use the connection from django db instead creating a new one
# connection = sqlite3.connect("db.sqlite3", check_same_thread=False)


def home(request):
    return render(request, "index.html")


def update_part(request, part_id):
    # The request body was not being accepted by the json.loads(). I decoded it as a string to fix the error
    part = json.loads(request.body.decode("utf-8"))
    # this table is part of the ERP application, so I can't create a model for it, because it tries to create migrations
    value_pairs = ",".join(
        (
            "{key}='{value}'".format(key=key, value=value)
            if isinstance(value, (str, bool))
            else "{key}={value}".format(key=key, value=value)
            for key, value in part.items()
        )
    )
    try:
        # I added this closing call from contextlib to fix a cursor calling error
        with closing(connection.cursor()) as cursor:
            cursor.execute(
                "UPDATE part SET {value_pairs} WHERE id={part_id}".format(
                    value_pairs=value_pairs, part_id=part_id
                )
                # The table name was wrong
            )
    except Exception as e:
        return HttpResponse(status=500, content=e)

    return HttpResponse(status=200)
