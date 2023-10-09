from rest_framework import viewsets, status
from .models import PredictionResult
from .serializers import PredictionResultSerializer
from rest_framework.response import Response

class PredictionResultViewSet(viewsets.ModelViewSet):
    queryset = PredictionResult.objects.all()
    serializer_class = PredictionResultSerializer
    