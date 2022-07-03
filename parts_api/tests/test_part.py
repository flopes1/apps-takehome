from django.test import TestCase, Client
from django.db import connection
from contextlib import closing
from rest_framework import status

import json

from parts_api.models import Part
from parts_api.api.serializers import PartSerializer

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


class PartViewV2Tests(TestCase):
    """ Test class for the new Part endpoint using DRF """

    def setUp(self):
        self.client = Client()

    def test_get_all_parts(self):
        all_parts = Part.objects.all()
        serializer = PartSerializer(all_parts, many=True)

        response = self.client.get("/part/v2/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_part_by_id(self):
        part = Part.objects.get(id=1)

        response = self.client.get("/part/v2/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], part.id)
        self.assertEqual(response.data["name"], part.name)

    def test_add_part(self):
        payload = {"name": "part name", "sku": "part sku", "description": "part description", "weight_ounces": 7,
                   "is_active": 1}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["description"], payload["description"])

    def test_add_invalid_part(self):
        payload = {"name": "part name"}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_part(self):
        payload = {"name": "part name", "sku": "part sku", "description": "part description", "weight_ounces": 7,
                   "is_active": 1}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["description"], payload["description"])

        updated_payload = {"name": "part name 2", "sku": "part sku", "description": "part description",
                           "weight_ounces": 7, "is_active": 1}

        created_part_id = response.data["id"]

        response = self.client.put("/part/v2/{}/".format(created_part_id), json.dumps(updated_payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], updated_payload["name"])
        self.assertEqual(response.data["description"], updated_payload["description"])

    def test_update_part_missing_attribute(self):
        payload = {"name": "part name", "sku": "part sku", "description": "part description", "weight_ounces": 7,
                   "is_active": 1}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["description"], payload["description"])

        updated_payload = {"name": "part name 2"}

        created_part_id = response.data["id"]

        response = self.client.put("/part/v2/{}/".format(created_part_id), json.dumps(updated_payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_part(self):
        payload = {"name": "part name", "sku": "part sku", "description": "part description", "weight_ounces": 7,
                   "is_active": 1}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["description"], payload["description"])

        created_part_id = response.data["id"]

        response = self.client.delete("/part/v2/{}/".format(created_part_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_missing_part(self):
        response = self.client.delete("/part/v2/{}/".format(99))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_part(self):
        payload = {"name": "part name", "sku": "part sku", "description": "part description", "weight_ounces": 7,
                   "is_active": 1}

        response = self.client.post("/part/v2/", json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["description"], payload["description"])

        updated_payload = {"name": "part name 2"}

        created_part_id = response.data["id"]

        response = self.client.patch("/part/v2/{}/".format(created_part_id), json.dumps(updated_payload),
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], updated_payload["name"])
