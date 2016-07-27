from django.shortcuts import render, redirect, HttpResponse
from .models import Item
from ..users.models import User, Validator
import bcrypt
# Create your views here.
def index(request):
	if 'user_id' not in request.session:
		return redirect("lr_page")

	curUser = User.objects.get(id=request.session["user_id"])
	context = {
		"self_wl_items": Item.objects.filter(creator=curUser) | Item.objects.filter(coowners=curUser.id),
		"other_wl_items": Item.objects.exclude(creator=curUser).exclude(coowners=curUser.id),
		"name": curUser.name,
	}
	return render(request, 'wish_list/index.html', context)
def new(request):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	return render(request, 'wish_list/add_wish_item.html')
def show(request, item_id):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	item = Item.objects.get(id=item_id)
	context = {
		'item': item
	}
	return render(request, 'wish_list/show_item.html', context)
def add_to_mine(request, item_id):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	user = User.objects.get(id=request.session["user_id"])
	item = Item.objects.get(id=item_id)
	item.coowners.add(user)
	return redirect("wish_list")
def remove_from_mine(request, item_id):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	user = User.objects.get(id=request.session["user_id"])
	item = Item.objects.get(id=item_id)
	item.coowners.remove(user)
	return redirect("wish_list")
def create(request):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	
	validator = Validator()
	formInput = {'item_name': 3}
	validator.isShort(request.POST, formInput)
	if validator.error:
		context = {
			'msg': validator.msg
		}
		return render(request, 'wish_list/add_wish_item.html', context)
	Item.objects.create(name=request.POST['item_name'], creator=User.objects.get(id=request.session['user_id']))
	return redirect('wish_list')
def delete(request, item_id):
	if 'user_id' not in request.session:
		return redirect("lr_page")
	Item.objects.get(id=item_id).delete()
	return redirect("wish_list")