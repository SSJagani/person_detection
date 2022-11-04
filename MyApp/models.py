from django.db import models

# Create your models here.
class User(models.Model):
	user_no = models.AutoField(primary_key=True)
	user_id = models.IntegerField(default="")
	user_name = models.CharField(max_length=90,default="" )

	def __str__(self):
		return self.user_name