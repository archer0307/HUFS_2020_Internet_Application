from django.db import models

# Create your models here.
class ClientData(models.Model):
	identification = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=11)
	name = models.CharField(max_length=20)
	
	

	def __str__(self):
		return {'identification':self.identification,'password':self.password,'phone_number':self.phone_number,'name':self.name}
