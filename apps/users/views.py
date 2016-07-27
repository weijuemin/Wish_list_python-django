from django.shortcuts import render, redirect, HttpResponse
from .models import User, Validator, UserManager
import bcrypt
# Create your views here.
def login_page(request):
	return render(request, "users/index.html")

def login(request):
	if request.method != "POST":
		return redirect("login_page")
	validator = Validator()
	usermanager = UserManager()
	formInput = {'username': 1, 'password': 1}
	validator.isShort(request.POST, formInput)
	if not validator.error:
		if not usermanager.exist(request.POST):
			request.session['exist'] = False
			validator.msg['notExist'] = 'This username has not registered. Please register first'
			context = {
				'msg': validator.msg
			}
			return render(request, 'users/index.html', context)
		else:
			curUser = User.objects.get(username=request.POST['username'])
			if bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8'), curUser.password.encode(encoding='utf-8')) == curUser.password.encode(encoding='utf-8'):
				context = {
					'curUser': curUser
				}
				request.session['name'] = curUser.name
				request.session['user_id'] = curUser.id
				return redirect("wish_list")
			else:
				validator.msg['pwErr'] = 'Password incorrect!'
	context = {
				'msg': validator.msg
			}
	return render(request, 'users/index.html', context)

def register(request):
	if request.method != "POST":
		return redirect("login_page")
	validator = Validator()
	usermanager = UserManager()
	formInput = {'name': 3, 'username':3, 'password': 8}
	validator.isShort(request.POST, formInput)
	user = User.objects.filter(username=request.POST["username"])
	if not validator.error:
		if usermanager.exist(request.POST):
			request.session['exist'] = True
			validator.msg['exist'] = 'This username has registered already. Please log in'
			context = {
				'msg': validator.msg
			}
			return render(request, 'users/index.html', context)
		pw_hash = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8'), bcrypt.gensalt())
		User.objects.create(name=request.POST['name'], username=request.POST['username'], password=pw_hash)
		curUser = User.objects.get(username=request.POST['username'])
		context = {
			'curUser': curUser
		}
		request.session['name'] = curUser.name
		request.session['user_id'] = curUser.id
		return redirect("wish_list")
	context = {
		'msg': validator.msg
	}
	return render(request, 'users/index.html', context)

def logout(request):
	request.session.clear()
	return redirect("lr_page")