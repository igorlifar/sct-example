from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('styles.views',
	url(r'^index.css$', 'index'),
#	url(r'^mypage.css$', 'index'),
#	url(r'^member.css$', 'index'),
)