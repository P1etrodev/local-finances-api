from django.db import models

from transactions.models import Transaction


# Create your models here.
class Person(models.Model):
	created_at = models.DateField(auto_now_add=True)
	name = models.TextField(max_length=20)
	
	@property
	def transactions(self):
		return self.transaction_set.all()
	
	@property
	def borrowed(self) -> float:
		transactions: models.QuerySet[Transaction] = self.transactions
		total: float = sum(
			payment.amount
			for payment in transactions
			if payment.type == 'borrow'
		)
		return total
	
	@property
	def lended(self) -> float:
		transactions: models.QuerySet[Transaction] = self.transactions
		total: float = sum(
			payment.amount
			for payment in transactions
			if payment.type == 'lend'
		)
		return total