from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200) 
	url = models.CharField(max_length=200) 
	tab_pdf = models.FileField(default="") 
	tab_gp = models.FileField(default="") 

	def __str__(self):
		return self.title