from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('',
    (r'^(?P<page_name>[^/]+)/edit/$','wiki.views.edit_page'),
    (r'^(?P<page_name>[^/]+)/save/$','wiki.views.save_page'),
    (r'^(?P<page_name>[^/]+)/$','wiki.views.view_page'),
)

