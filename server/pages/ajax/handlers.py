from django.http import HttpResponse
import json
from pages.sections import get_path_section as get_html_section
from scripts.sections import get_path_section as get_js_section
from pages.shortcuts import render_template as render_html_template
from scripts.shortcuts import render_js_template
from pages.context import get_context

def get_page_part(request):
	
	req = json.loads(request.raw_post_data)
	h_section = get_html_section(req['path'], request)
	h_context = get_context(h_section, request)
		
	j_section = get_js_section('scripts/' + h_context['js'], request)
	
	h_template = req['template']
	
	response = {}
	response["html"] = render_html_template(section = h_section, context = h_context, request = request, template = h_template)
	
	try:
		response["js"] = render_js_template(section = j_section, context = {}, request = request, template = h_template[:-5] + '.js')
	except:
		response['js'] = ''
		
	return HttpResponse(json.dumps(response))	