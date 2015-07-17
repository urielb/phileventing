from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'category/(?P<category>\w+)/(?P<cat_id>\d+)/$', 'events_by_category', name='events_by_category'),
)