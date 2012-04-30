from django.http import Http404

def get_path_section(path, request):
	path = ("/index/" + path).strip('/').split('/')[1:]
	l = len(path)
	
	if l == 0:
		return ['index']
	
	raise Http404

def get_section(request):
	return get_path_section(request.path, request)