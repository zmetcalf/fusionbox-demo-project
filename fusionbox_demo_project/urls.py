from django.conf.urls import patterns, include, url
from django.contrib import admin

from fusionbox_demo_project.widgy_site import site as widgy_site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # widgy admin
    url(r'^admin/widgy/', include(widgy_site.urls)),
    # widgy frontend
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),
    url(r'^', include('mezzanine.urls')),
    url(r'^$', 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),
)
