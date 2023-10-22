from rest_framework.routers import DefaultRouter
from .views import PredictionsViewSet

router = DefaultRouter()
router.register(r'predictions', PredictionsViewSet, basename='predictions')

urlpatterns = [

]

urlpatterns += router.urls
