from django.db import models

# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length=30, blank=False)
	message = models.CharField(max_length=200, blank=False)
	date = models.DateField(auto_now=True)

class Comments(models.Model):
	post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
	message = models.CharField(max_length=200, blank=False)
	date = models.DateField(auto_now=True)