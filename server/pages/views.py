from pages.shortcuts import render_to_response as render
from pages.site.nodes import RootNode

def index(request):

	root = RootNode(request)
	section = root.get_section()
	context = root.get_context()
	
	return render(section, context, request)