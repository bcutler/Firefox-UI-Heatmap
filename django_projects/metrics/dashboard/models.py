from django.db import models

# Create your models here.
class Heatmap(models.Model):
	item_name = models.CharField(max_length=100)
	freq = models.IntegerField()
	freq_per_user = models.DecimalField(max_digits=5, decimal_places=5)
	perc = models.DecimalField(max_digits=5, decimal_places=5)	
	in_table = models.BooleanField()
	os = models.CharField(max_length=100)
	skill = models.CharField(max_length=100)
	
	def heat(self):
    #$normalize = (log($freq+1)/log($max))
    #$h = 360 * (1 - $normalize)
    #$s = $normalize * 75
    #$l = $normalize * 50
    #return "hsl(" .$h ."," .$s ."%," .$l ."%)"	
		return true
		
	
	def __unicode__(self):
		return 'A heatmap of id %d' % (self.id)