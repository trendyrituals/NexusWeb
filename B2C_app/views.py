from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'B2C/home.html',{})
