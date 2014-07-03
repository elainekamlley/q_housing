from django.db import models

# Create your models here.

#Relationships:
#==================
# One to Many:
#	One User can provide Many Houses
#	One User can review Many Reviews
#==================
# Many to Many:
# 	Many Users can have Many Identities
#	Many Users can stay at Many Houses
# 	Many Houses can have Many Users stay


class User(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField(max_length= 250)
	password = models.CharField(max_length=100)
	role = models.CharField(max_length=100)

	def __unicode__(self):
		return self.first_name

class Identities(models.Model):
	age = models.IntegerField(default=0)
	gender = models.CharField(max_length=50)
	race = models.CharField(max_length=100)
	sexual_orientation = models.CharField(max_length = 100)
	user_id = models.ManyToManyField(User)

	def __unicode__(self):
		return self.user_id

class Houses(models.Model):#best practice is to create singular name
	description = models.CharField(max_length = 300)
	user_id = models.ForeignKey(User)
	status = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	room_type = models.CharField(max_length = 100)
	min_stay = models.IntegerField(default=0)
	max_stay = models.IntegerField(default=0)
	booker_id = models.IntegerField(default=0)
	created_at = models.DateTimeField('date created')
	updated_at = models.DateTimeField('date updated')

	def __unicode__(self):
		return self.user_id

class Booking(models.Model):
	check_in = models.DateTimeField('check in')
	check_out = models.DateTimeField('check out')
	house_id = models.ForeignKey(Houses)
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField('date created')
	updated_at = models.DateTimeField('date updated')

class Reviews(models.Model):
	reviewer = models.ForeignKey(User)
	content = models.CharField(max_length = 400)


