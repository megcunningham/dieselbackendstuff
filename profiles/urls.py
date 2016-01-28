from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import UserView


router = routers.DefaultRouter()
router.register(r'profiles', UserView, 'list')

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
