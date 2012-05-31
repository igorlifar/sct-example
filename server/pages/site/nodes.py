from pages.sections import SectionNode
from index.nodes import IndexNode

class RootNode(SectionNode):
	def __init__(self, request):
		path = ('root' + request.path).strip('/').split('/')[1:] # little trick to get empty list in case of '/' path
		if len(path) == 0:
			self.child = IndexNode(request, path)

