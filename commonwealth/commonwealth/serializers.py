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
        wage_score = BusinessSerializer.compute_wage_score(actual_wage)
        validated_data['wage_score'] = wage_score

        # compute the coin score and set it
        coin_score = BusinessSerializer.compute_coin_score(wage_score, validated_data['transportation_score'])
        validated_data['coin_score'] = coin_score

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.actual_wage = validated_data.get('actual_wage', 
                instance.actual_wage)
        wage_score = BusinessSerializer.compute_wage_score(instance.actual_wage)
        coin_score = BusinessSerializer.compute_coin_score(wage_score, 
                instance.transportation_score)

        instance.wage_score = wage_score
        instance.coin_score = coin_score

        instance.save()

        return instance

    def compute_wage_score(actual_wage):
        return (actual_wage - BusinessSerializer.min_wage)/(BusinessSerializer.mit_wage - BusinessSerializer.min_wage)

    def compute_coin_score(wage_score, transportation_score):
        return wage_score * (1 - transportation_score)
