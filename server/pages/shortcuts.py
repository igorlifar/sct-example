from django.core.context_processors import csrf
from django.template import Context, loader
from django.conf import settings
from django.http import HttpResponse

from server.settings import sct_root_html_template as root_html_template

def render_template(section, context, request, template):
	
	context.update({'s': section})
	context.update({'static':  '/static_files/'})
	context.update(csrf(request))
	
	t = loader.get_template(template)
	c = Context(context)
	return t.render(c)
	
def render(section, context, request):
	return render_template(section, context, request, root_html_template)
	
def render_template_to_response(section, context, request, template):
	return HttpResponse(render_template(section, context, request, template))
	
def render_to_response(section, context, request):
	return HttpResponse(render(section, context, request))
