from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		context = {
			'username': request.user.username
		}
		return render(request,'superuser/home.html',context)
	else:
		return redirect('/auth/login/')