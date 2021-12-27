from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	get_user_model
	)
from django.contrib.auth.models import Group
from .forms import LoginForm, Register_Form
from .models import ExtendUser

User = get_user_model()
# Create your views here.
def login_view(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		try:
			login(request,user)
			return redirect('/auth/check/')
		except:
			return redirect('/auth/login/')
	context = {
	
	}
	return render(request,'auth/login.html',context)





def check(request):
	grp = request.user.groups.get()
	B2B = Group.objects.get(name='B2B')
	B2C = Group.objects.get(name='B2C')
	SUPER = Group.objects.get(name='superuser')
	AGENT = Group.objects.get(name='agent')
	B2E = Group.objects.get(name='B2E')
	if grp==B2B:
		return redirect('/B2B/')
	elif grp==B2C:
		return redirect('/B2C/')
	elif grp==SUPER:
		return redirect('/super/')
	elif grp==AGENT:
		return redirect('/agent/')
	elif grp==B2E:
		return redirect('/B2E/')
	else:
		return redirect('/auth/login/')






def logout_(request):
	logout(request)
	return redirect('/auth/login')






def sign_view_B2B(request):
	if request.user.is_authenticated:
		#register a new B2B type user
		form = Register_Form(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			confirm_password = form.cleaned_data.get('confirm_password')
			if password == confirm_password:
				user.set_password(password)
				user.save()
				user_group = Group.objects.get(name='B2B')
				user.groups.add(user_group)
				new = ExtendUser()
				new.r = user
				new.added_by = request.user
				new.save()

				form = Register_Form()
		context = {
		'form':form
		}
		return render(request,'auth/sign_up_B2B.html',context)
	else:
		return redirect('/auth/login/')




def sign_view_B2C(request):
	if request.user.is_authenticated:
		#register a new B2C type user
		form = Register_Form(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			confirm_password = form.cleaned_data.get('confirm_password')
			if password == confirm_password:
				user.set_password(password)
				user.save()
				user_group = Group.objects.get(name='B2C')
				user.groups.add(user_group)
				new = ExtendUser()
				new.r = user
				new.added_by = request.user
				new.save()

				form = Register_Form()
		context = {
		'form':form
		}
		return render(request,'auth/sign_up_B2C.html',context)
	else:
		return redirect('/auth/login/')




def sign_view_B2E(request):
	if request.user.is_authenticated:
		#register a new B2E type user
		form = Register_Form(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			confirm_password = form.cleaned_data.get('confirm_password')
			if password == confirm_password:
				user.set_password(password)
				user.save()
				user_group = Group.objects.get(name='B2E')
				user.groups.add(user_group)
				new = ExtendUser()
				new.r = user
				new.added_by = request.user
				new.save()

				form = Register_Form()
		context = {
		'form':form
		}
		return render(request,'auth/sign_up_B2E.html',context)
	else:
		return redirect('/auth/login/')




def sign_view_agent(request):
	if request.user.is_authenticated:
		#register a new agent type user
		form = Register_Form(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			confirm_password = form.cleaned_data.get('confirm_password')
			if password == confirm_password:
				user.set_password(password)
				user.save()
				user_group = Group.objects.get(name='agent')
				user.groups.add(user_group)
				new = ExtendUser()
				new.r = user
				new.added_by = request.user
				new.save()

				form = Register_Form()
		context = {
		'form':form
		}
		return render(request,'auth/sign_up_agent.html',context)
	else:
		return redirect('/auth/login/')
