from django.db import models
from math import log

# Create your models here.
class Heatmap(models.Model):
	item = models.CharField(max_length=100)
	category= models.CharField(max_length=100)	
	os = models.CharField(max_length=30)		
	skill = models.CharField(max_length=30)	
	time_on_web = models.IntegerField()	
	perc = models.DecimalField(max_digits=5, decimal_places=5)
	clicks_per_user = models.DecimalField(max_digits=5, decimal_places=5)
	clicks_per_user_median =models.DecimalField(max_digits=5, decimal_places=5)
	
	def heat_perc(self):
		normalize = log((self.perc * 100) + 1 )/ log(100)
		h = 360 * (1 - normalize)
		s = normalize * 75
		l = normalize * 50
		return "hsl(" + str(h) + "," + str(s) +"%," + str(l) + "%)"	
		
	def __unicode__(self):
		return 'A heatmap of id %d' % (self.id)