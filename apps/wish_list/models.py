from django.db import models
from ..users.models import User

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	creator = models.ForeignKey(User, related_name="creator")
	coowners = models.ManyToManyField(User, related_name="coowners")