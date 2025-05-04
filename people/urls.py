from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import PeopleViewSet

router = DefaultRouter()
router.register(r'', PeopleViewSet)

urlpatterns = [
	path(r'', include(router.urls))
]