from styles.sections import get_section
from styles.shortcuts import render

def index(request):
	print "test2"
	section = get_section(request)
	return render(section, request)