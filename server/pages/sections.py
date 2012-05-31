class SectionNode(object):

	child = None
	local_section = []

	def _get_local_context(self):
		return {}

	def get_context(self):
		
		context = self._get_local_context()

		if self.child:
			context.update(self.child.get_context())

		return context

	def get_section(self):
		section = self.local_section
		if self.child:
			section += self.child.get_section()

		return section


