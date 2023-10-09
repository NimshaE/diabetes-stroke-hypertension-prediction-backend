from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PredictionsViewSet

router = DefaultRouter()
router.register(r'predictions', PredictionsViewSet, basename='predictions')

urlpatterns = [
    # Add your other app URLs here if any
]

urlpatterns += router.urls
