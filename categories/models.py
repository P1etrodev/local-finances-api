from django.db import models

from transactions.models import Transaction


class Category(models.Model):
	name = models.TextField(unique=True)
	color = models.TextField(unique=True)
	
	@property
	def amount(self):
		qs = Transaction.objects.filter(category__id=self.id)
		return len(qs)