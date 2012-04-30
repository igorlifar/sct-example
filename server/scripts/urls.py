from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('scripts.views',
	url('^index.js$', 'index'),
#	url(r'^mypage-profile.js$', 'index'),
#	url(r'^mypage-messages.js', 'index'),
)