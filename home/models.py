from django.db import models

class post(models.Model):
	title = models.CharField(max_length=100,null =True)
	user = models.CharField(max_length=100,null =True)
	entry = models.TextField(max_length=3000)
	date = models.DateTimeField('date posted')
	happiness_index = models.FloatField(null=True, blank=True, default=0.0)
	angry_index = models.FloatField(null=True, blank=True, default=0.0)
	bored_index = models.FloatField(null=True, blank=True, default=0.0)
	sad_index = models.FloatField(null=True, blank=True, default=0.0)
	fear_index = models.FloatField(null=True, blank=True, default=0.0)
	exited_index = models.FloatField(null=True, blank=True, default=0.0)
	dep = models.FloatField(null=True, blank=True, default=0.0)
	
