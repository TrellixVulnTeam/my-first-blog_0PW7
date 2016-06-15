from django.shortcuts import render

# Create your views here.

def post_list(request):
	return render(request, 'blog/post_list.html',{})

def irshadlanding(request):
	return render(request, 'blog/stud-home.html',{})
