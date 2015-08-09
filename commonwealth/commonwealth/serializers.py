from .models import Business

from rest_framework import serializers

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('yelp_id', 'business_name', 'lat', 'lon',
                'address', 'image_url', 
                'coin_score', 'wage_score', 'actual_wage',
                'transportation_score')
