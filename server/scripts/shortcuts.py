from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

from server.settings import sct_root_js_template as root_js_template
	
def render_js_template(section, request, template):
	context = {'section': section}
	t = loader.get_template(template)
	c = Context(context)
	return t.render(c)

def render_js(section, request):
	return render_template(section, request, root_js_template)
	
def render_js_template_to_response(section, request, template):
	return HttpResponse(render_js_template(section, request, template),  mimetype="text/javascript; charset=utf-8")
	
def render_js_to_response(section, request):
	return render_js_template_to_response(section, request, root_js_template)