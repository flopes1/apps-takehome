import json
import unittest
from takehome import views
import sqlite3

class HttpRequest(object):
    def __init__(self, body):
        self._body = body
        
    @property
    def body(self):
        return json.dumps(self._body)
     
class HttpResponse(object):
    def __init__(self, content=b'', content_type=None, status=200, reason=None, charset=None):
        self._content = content
        self._status = status
        
    @property
    def content(self):
        return self._content
    
    @property
    def status(self):
        return self._status

connection = sqlite3.connect("db.sqlite3")

class PartViewTests(unittest.TestCase):
    def test_update_part(self):
        pass  # TODO write test
