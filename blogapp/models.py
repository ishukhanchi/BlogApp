from django.db import models

# Create your models here.

class blog(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	content = models.CharField(max_length=3000)
	blog_image = models.ImageField()


	def __str__(self):
		return self.title.lower()
