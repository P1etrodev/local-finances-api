from django.db import models


class Transaction(models.Model):
	class TransactionType(models.TextChoices):
		INCOME = 'income'
		EXPENSE = 'expense'
		LEND = 'lend'
		BORROW = 'borrow'
	
	date = models.DateField()
	summary = models.TextField()
	type = models.TextField(choices=TransactionType)
	category = models.ForeignKey('categories.Category', models.DO_NOTHING)
	person = models.ForeignKey(
		'people.Person',
		models.CASCADE,
		null=True,
		blank=True,
		default=None,
	)
	amount = models.PositiveIntegerField()