from django.db import models

class Room(models.Model):
	"""
	docstring for Rooms.
	Este es el modelo de la clase Rooms.
	la url tiene que ser /room/id/sensor/id
	"""
	"tiene que tener ID PrimaryKey "
	owner = models.ForeignKey('auth.User', related_name='rooms')
	created = models.DateTimeField(auto_now_add=True)
	roomName = models.CharField(max_length=100, blank=False)
	#sensors = models.ForeignKey('freedom.Sensor', related_name='rooms', null='True')
	"tiene que tener sensores"

	def __unicode__(self):
		return self.roomName

	def save(self, *args, **kwargs):
	    super(Room, self).save(*args, **kwargs)

	class Meta:
		"""
		los ordena por algun criterio
		por ahora esta por criterio de creacion
		podria estar ordenado por nombre o id
		"""
		ordering = ('created',)

class Sensor(models.Model):
	"""
	docstring for Sensor.
	Este es el modelo de la clase Sensor.
	la url tiene que ser /room/id/sensor/id
	"""
	"tiene que tener ID PrimaryKey "
	owner = models.ForeignKey('auth.User', related_name='sensors')
	room = models.ForeignKey(Room, related_name='sensors')
	created = models.DateTimeField(auto_now_add=True)
	sensorName = models.CharField(max_length=100, blank=False)

	def save(self, *args, **kwargs):
	    super(Sensor, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('sensorName','room')
		ordering = ('created',)