from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="wish_list"),
	url(r'^add_wish_item$', views.new, name="new_wish"),
	url(r'^create', views.create, name="create_wish"),
	url(r'^show_wish_item/(?P<item_id>\d+)$', views.show, name="show_item"),
	url(r'^add/item/(?P<item_id>\d+)$', views.add_to_mine, name="add_to_mine"),
	url(r'^remove/item/(?P<item_id>\d+)$', views.remove_from_mine, name="remove_from_mine"),
	url(r'^delete/item/(?P<item_id>\d+)$', views.delete, name="delete")
]