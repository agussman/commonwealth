from django.db import models

class Business(models.Model):
    yelp_id = models.IntegerField()
    overall_score = models.IntegerField(default=0)
    certification_level = models.CharField(max_length=200)
