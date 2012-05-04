from django.http import Http404


class SectionException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


def get_path_section(path, request):
	path = ('/index' + path).strip('/').split('/')[1:]
	l = len(path)

	if l == 0:
		return ['index']

	raise Http404


def get_section(request):
	return get_path_section(request.path, request)
