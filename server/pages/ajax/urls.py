from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('ajax.paging.handlers',
	url(r'^get_page_part/', 'get_page_part'),
)