from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login', 'django.contrib.auth.views.login', name='my_login'),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout', name='my_logout'),
    # Examples:
    # url(r'^$', 'my_project.views.home', name='home'),
    # url(r'^my_project/', include('my_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'events.views.index', name='index'),
    url(r'^events/', include('events.urls')),
    url(r'^accounts/', include('accounts.urls')),
)


from app.views import home, done, logout, error, form, form2
from app.facebook import facebook_view

urlpatterns += patterns('',
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'', include('social_auth.urls')),
)
