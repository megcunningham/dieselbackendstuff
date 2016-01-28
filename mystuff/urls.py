"""mystuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from workouts.views import get_arms, get_back, get_chest, get_legs, get_shoulders, weekly_workout, search_names


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/arms/', get_arms),
    url(r'^api/back/', get_back),
    url(r'^api/chest/', get_chest),
    url(r'^api/legs/', get_legs),
    url(r'^api/shoulders/', get_shoulders),
    url(r'^api/weekly_workout/', weekly_workout),
    url(r'^api/search/', search_names),
    url(r'^api/profiles/', include('profiles.urls'))
]
