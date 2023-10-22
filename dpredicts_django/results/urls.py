from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'results', views.PredictionResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('results/', views.PredictionResultListView.as_view(), name='prediction-result-list'),
]