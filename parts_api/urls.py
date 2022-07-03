from django.contrib import admin
from django.conf.urls import include, url
from parts_api import views

# I had to change the urls order because when the one with empty path was in the first position
# the other endpoints were not being loaded
urlpatterns = [
    url("admin/", admin.site.urls),
    url("part/update/(?P<part_id>\d+)/$", views.update_part),
    url("", views.home, name="home"),
]

