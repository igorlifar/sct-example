from pages.sections import SectionNode

class IndexNode(SectionNode):
	def __init__(self, request, path):
		self.local_section = 'index'
