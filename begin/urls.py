from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'posts.views.home', name='home'),

    # url(r'^categories/$', 'posts.views.categories', name='categories'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[a-zA-Z0-9\-]+)/$',
        'posts.views.detail', name='detail')
)
