from django.test import TestCase, Client
from django.db import connection
from contextlib import closing

import json

from parts_api import views
from parts_api.tests.utils import HttpRequest, HttpResponse

# connection = sqlite3.connect("db.sqlite3", check_same_thread=False)


class PartViewTests(TestCase):

    def setUp(self):
        self.connection = connection
        self.client = Client()
        self.stub_part = {
            "name": "Macrochip",
            "sku": "OWDD823011DJSD",
            "description": "Used for heavy-load computing",
            "weight_ounces": 2,
            "is_active": 1,
        }
        self.add_stub_part()

    def test_update_part(self):
        part = self.get_part(4)

        self.assertEqual(part[0], 4)
        self.assertEqual(part[1], self.stub_part["name"])

        response = self.client.put("/part/update/4/", json.dumps({"name": "New Name"}))

        self.assertEqual(response.status_code, 200)

        updated_part = self.get_part(4)
        self.assertEqual(updated_part[1], "New Name")

    def add_stub_part(self):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(
                """INSERT INTO part VALUES (4, "{}", "{}", "{}", {}, {}) \
                            """.format(self.stub_part["name"], self.stub_part["sku"], self.stub_part["description"],
                                       self.stub_part["weight_ounces"], self.stub_part["is_active"])
                )

    def get_part(self, part_id):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(
                "SELECT * FROM part where id = {}".format(
                    part_id
                ))
            part = cursor.fetchall()
        return part[0]
