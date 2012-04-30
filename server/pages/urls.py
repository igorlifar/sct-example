from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pages.views',
	url(r'^ajax/', include('pages.ajax.urls')),
	url(r'^', 'index'),
)