from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import PredictionResult
from .serializers import PredictionResultSerializer

class PredictionResultViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('predictionresult-list')
    def test_list_prediction_results(self):
        prediction_result1 = PredictionResult.objects.create(
            patient_name='Anne Perera',
            note='Patient is in a risk of Diabetes',
            diabetes_prediction='Yes',
            hypertension_prediction='No',
            stroke_prediction='No'
        )
        prediction_result2 = PredictionResult.objects.create(
            patient_name='Kylie Dias',
            note='Instructed to constant blood pressure checkup',
            diabetes_prediction='No',
            hypertension_prediction='Yes',
            stroke_prediction='No'
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = PredictionResultSerializer([prediction_result1, prediction_result2], many=True).data
        self.assertEqual(response.data, serialized_data)

class PredictionResultListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('predictionresult-list')

    def test_list_prediction_results(self):
        prediction_result1 = PredictionResult.objects.create(
            patient_name='Angeline Perera',
            note='Instructed to blood sugar checkup',
            diabetes_prediction='Yes',
            hypertension_prediction='No',
            stroke_prediction='No'
        )
        prediction_result2 = PredictionResult.objects.create(
            patient_name='Gayle Peterson',
            note='Patient is in the risk of high blood pressure',
            diabetes_prediction='No',
            hypertension_prediction='Yes',
            stroke_prediction='No'
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = PredictionResultSerializer([prediction_result1, prediction_result2], many=True).data
        self.assertEqual(response.data, serialized_data)
