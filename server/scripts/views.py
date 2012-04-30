from scripts.sections import get_section
from scripts.shortcuts import render_js_to_response as render

def index(request):
	section = get_section(request)
	return render(section, request)