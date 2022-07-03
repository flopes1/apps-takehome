from django.contrib import admin
from django.conf.urls import include, url
from parts_api import views

from rest_framework import routers
from parts_api.api import viewsets as part_view_sets

route = routers.DefaultRouter()

route.register("v2", part_view_sets.PartViewSet, basename="Part")

# I had to change the urls order because when the one with empty path was in the first position
# the other endpoints were not being loaded
urlpatterns = [
    url("admin/", admin.site.urls),
    url("part/update/(?P<part_id>\d+)/$", views.update_part),
    url("part/", include(route.urls)),
    url("", views.home, name="home"),
]
