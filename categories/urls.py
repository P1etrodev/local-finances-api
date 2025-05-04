from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import CategoriesViewSet

router = DefaultRouter()
router.register(r'', CategoriesViewSet)

urlpatterns = [
	path('', include(router.urls))
]