from django.test import TestCase
import sqlite3
from takehome import views
from takehome.tests.utils import HttpRequest, HttpResponse

connection = sqlite3.connect("db.sqlite3")


class PartViewTests(TestCase):
    def test_update_part(self):
        pass  # TODO write test
