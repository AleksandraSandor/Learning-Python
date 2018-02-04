from django.shortcuts import render
from django.http import	HttpResponse

# Create your views here.
def	show_number(request, number):
	html = """
	<html>
		<body>
			<p>The	answer	is	%s!</p>
		</body>
	</html>
	"""	%	number
	return	HttpResponse(html)
#-------------------------str 38