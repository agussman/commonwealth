from .models import Business
import random
from rest_framework import serializers

class BusinessSerializer(serializers.ModelSerializer):
    mit_wage = 1484
    min_wage = 725
    class Meta:
        model = Business
        fields = ('yelp_id', 'business_name', 'lat', 'lon',
                'address', 'image_url', 
                'coin_score', 'wage_score', 'actual_wage',
                'transportation_score')

    def create(self, validated_data):
        # TODO: replace with real data
        random.seed()
        actual_wage = random.randint(725, 2275)
        validated_data['actual_wage'] = actual_wage / 100.0

        # compute the wage score and set it
        wage_score = (actual_wage - BusinessSerializer.min_wage)/(BusinessSerializer.mit_wage - BusinessSerializer.min_wage)
        validated_data['wage_score'] = wage_score

        # compute the coin score and set it
        coin_score = wage_score * (1 - validated_data['transportation_score'])
        validated_data['coin_score'] = coin_score

        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("UPDATE")
        print(repr(instance))
        print(repr(validated_data))

        #return super().update(instance, validated_data)
