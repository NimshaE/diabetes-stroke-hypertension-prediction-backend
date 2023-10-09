from django.db import models

class PredictionResult(models.Model):
    patient_name = models.CharField(max_length=255)
    note = models.TextField()
    diabetes_prediction = models.CharField(max_length=50)
    hypertension_prediction = models.CharField(max_length=50)
    stroke_prediction = models.CharField(max_length=50)
    prediction_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.prediction_timestamp}"
