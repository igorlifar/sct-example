from django.http import Http404

def get_path_section(path, request):
	return path.replace('-', '/')[:-3].strip('/').split('/')[1:]
	
def get_section(request):
	return get_path_section(request.path, request)