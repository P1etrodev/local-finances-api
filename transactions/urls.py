from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import TransactionsViewSet

router = DefaultRouter()
router.register(r'', TransactionsViewSet)

urlpatterns = [
	path('', include(router.urls))
]