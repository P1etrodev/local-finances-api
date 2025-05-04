from people.models import Person
from rest_framework import permissions, viewsets
from .serializers import PersonSerializer


class PeopleViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	permission_classes = [permissions.AllowAny]