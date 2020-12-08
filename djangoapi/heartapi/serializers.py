from rest_framework import serializers
from .models import PredResults


class PredSerializer(serializers.ModelSerializer):

    class Meta:
        model = PredResults
        fields = '__all__'