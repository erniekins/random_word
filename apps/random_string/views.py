from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	# request.session.clear()
	if request.method == 'POST':	
		if 'visit' not in request.session:
			request.session['visit'] = 0
		else:
			request.session['visit'] += 1
		print(request.session['visit'])
	context = {
		'random_things': get_random_string(length=14)
	}
	return render(request,'random_string/index.html', context)

def reset(request):
	# print('Im in reset!')
	# del request.session['visit']
	if 'visit' in request.session:
		request.session['visit'] = 0
	else:
		'error'
	return redirect(index)