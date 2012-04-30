from pages.sections import get_section
from pages.context import get_context
from pages.shortcuts import render_to_response as render

def index(request):
	section = get_section(request)
	context = get_context(section, request)
	
	return render(section, context, request)