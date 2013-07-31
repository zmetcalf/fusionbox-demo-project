from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^widgy-mezzanine/', include('widgy.contrib.widgy_mezzanine.urls')),
)
