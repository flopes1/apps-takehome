from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from takehome import views

router = routers.DefaultRouter()
router.register(r"widgets", views.WidgetViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url('', views.home, name= 'home'),
    url('admin/', admin.site.urls),
    url('part/update/(?P<part_id>\d+)/$', views.update_part)
]
