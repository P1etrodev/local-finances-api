from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = [permissions.AllowAny]
	
	def create(self, request, *args, **kwargs):
		if request.data['type'] in ['lend', 'borrow'] and request.data['person'] is None:
			raise ValidationError('')
		return super().create(request, args, kwargs)