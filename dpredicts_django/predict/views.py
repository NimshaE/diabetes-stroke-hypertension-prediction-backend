from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import InputDataSerializer
import pickle
import logging
class PredictionsViewSet(viewsets.ViewSet):
    def create(self, request):
        logger = logging.getLogger("predict")
        serializer = InputDataSerializer(data=request.data)
        if serializer.is_valid():
            input_data = [[serializer.validated_data[field] for field in serializer.fields]]
            with open('actclinica_model', 'rb') as model_file:
                loaded_classifier = pickle.load(model_file)
                predictions = loaded_classifier.predict(input_data)

                diabetes_prediction = "Yes" if predictions[0][0] == 1 else "No"
                hypertension_prediction = "Yes" if predictions[0][1] == 1 else "No"
                stroke_prediction = "Yes" if predictions[0][2] == 1 else "No"

                return Response({
                    "Diabetes": diabetes_prediction,
                    "Hypertension": hypertension_prediction,
                    "Stroke": stroke_prediction,
                },
                    status=status.HTTP_200_OK)
        else:
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
