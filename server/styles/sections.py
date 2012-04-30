def get_section(request):
	return request.path.replace('-', '/')[:-4].strip('/').split('/')[1:]