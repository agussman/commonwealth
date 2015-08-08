from .models import Business

from rest_framework import serializers

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('yelp_id', 'overall_score', 'certification_level')
