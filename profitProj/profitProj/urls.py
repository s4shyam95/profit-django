from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profitProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'profit.views.register', name='Register'),
    url(r'^updateGCM/$', 'profit.views.updateGCM', name='updateGCM'),
)
