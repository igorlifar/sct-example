from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

from server.settings import sct_root_css_template as root_css_template

def render_css_to_response(template, context):
	t = loader.get_template(template)
	c = Context(context)
	return HttpResponse(t.render(c), mimetype="text/css; charset=utf-8")
	
def render(section, request):
	
	context = {}
	context.update({'section': section})
	context.update({"images": "/static_files/images/"})
	
	return render_css_to_response(root_css_template, context)