from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Validator(object): # not using manager here cuz it's not dealing any table level management
	def __init__(self):
		self.error = False
		self.msg = {}
	def isShort(self, form, formInput):
		for key, val in formInput.iteritems():
			if len(form[key]) < val:
				self.error = True
				self.msg[key] = '{} should be at least {} characters'.format(key, val)
		return (self.msg, self.error)

class UserManager(models.Manager): # still not table level, but straight forward
	def exist(self, form):
		testUser = User.objects.filter(username=form['username'])
		if testUser:
			return True
		return False			
	def logout(self, session):
		keyList = ['name','username','user_id']
		for key in keyList:
			if key in session:
				session.pop(key)
				
class User(models.Model):
	name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "User with name {}".format(self.name)