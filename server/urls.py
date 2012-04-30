from django.conf.urls.defaults import patterns, include, url
from local_settings import root_dir


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url('^scripts/', include('scripts.urls')),
	url('^styles/', include('styles.urls')),
	
	# use django.views.static.serve FOR DEVELOPMENT ONLY
	url(r'^static_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': root_dir + 'static_files/'}),	
	url(r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': root_dir + 'media_files/'}),
	
	url('^', include('pages.urls')),
	
    # url(r'^admin/', include(admin.site.urls)),
)
