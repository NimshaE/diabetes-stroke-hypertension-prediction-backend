from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import InputDataSerializer

class PredictionsViewSetTestCase(APITestCase):

    def test_create_prediction(self):
        input_data = {
            "Age": 4,
            "Sex": 1,
            "HighChol": 0,
            "BMI": 26,
            "Smoker": 0,
            "HeartDiseaseorAttack": 0,
            "PhysActivity": 1,
            "HvyAlcoholConsump": 0,
            "GenHlth": 3,
            "MentHlth": 5,
        }

        serializer = InputDataSerializer(data=input_data)
        self.assertTrue(serializer.is_valid(), f"Serializer errors: {serializer.errors}")

        url = reverse("predictions-list")
        response = self.client.post(url, input_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, {
            "Diabetes": "No",
            "Hypertension": "Yes",
            "Stroke": "Yes",
        })
