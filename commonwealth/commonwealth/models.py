from django.db import models

class Business(models.Model):
    yelp_id = models.IntegerField()
    business_name = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    address = models.TextField()
    image_url = models.CharField(max_length=500)
    coin_score = models.IntegerField(default=0)
    wage_score = models.IntegerField(default=0)
    actual_wage = models.IntegerField(default=0)
    transportation_score = models.IntegerField(default=0)
    #certification_level = models.CharField(max_length=200)
