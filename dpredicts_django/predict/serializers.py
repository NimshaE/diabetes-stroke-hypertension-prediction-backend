from rest_framework import serializers

class InputDataSerializer(serializers.Serializer):
    Age = serializers.FloatField()
    Sex = serializers.FloatField()
    HighChol = serializers.FloatField()
    BMI = serializers.FloatField()
    Smoker = serializers.FloatField()
    HeartDiseaseorAttack = serializers.FloatField()
    PhysActivity = serializers.FloatField()
    HvyAlcoholConsump = serializers.FloatField()
    GenHlth = serializers.FloatField()
    MentHlth = serializers.FloatField()
