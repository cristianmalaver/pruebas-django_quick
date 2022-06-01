from xml.dom.minidom import Document
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
								.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
								.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]

class Client(models.Model):
	document = models.IntegerField()   
	first_name = models.CharField(max_length=300)  
	last_name = models.CharField(max_length=300)  
	email = models.CharField(max_length=300)

	class Meta:
		indexes = [
		models.Index(fields=['first_name', 'last_name',]),
		]

	def __str__(self):
		return self.first_name

class Bill(models.Model):
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	company_name = models.CharField(max_length=300)
	nit = models.IntegerField()
	code = models.CharField(max_length=300)

	def __str__(self):
		return self.company_name

class Product(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=300)

	def __str__(self):
		return self.name

class Bill_Product(models.Model):
	bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.bill_id.code
	








