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
	name = models.CharField(max_length=100, blank=False)
	"tiene que tener sensores"

	def save(self, *args, **kwargs):
	    super(Room, self).save(*args, **kwargs)

	class Meta:
		"""
		los ordena por algun criterio
		por ahora esta por criterio de creacion
		podria estar ordenado por nombre o id
		"""
		ordering = ('created',)