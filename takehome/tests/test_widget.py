from django.conf.urls import include, url
from django.test import TestCase
from takehome import views
from takehome.tests.factories import WidgetFactory
from rest_framework.routers import DefaultRouter
from rest_framework.test import URLPatternsTestCase


class WidgetViewTests(TestCase, URLPatternsTestCase):
    router = DefaultRouter()
    router.register(r"widgets", views.WidgetViewSet)
    urlpatterns = [url(r"api/", include(router.urls))]
    base_url = "/api/widgets/"
    method = "GET"

    def test_widgets_returned(self):
        WidgetFactory(name="Spronk Lever")
        WidgetFactory(name="High Pressure Drasper")
        
        response = self.client.get(
            self.base_url,
            content_type="application/json",
        )
        widgets = response.json()
        widget_names = [w["name"] for w in widgets]
        
        self.assertIn("Spronk Lever", widget_names)
        self.assertIn("High Pressure Drasper", widget_names)
