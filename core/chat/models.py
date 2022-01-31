from django.db import models

# Create your models here.
class ChatRoom(models.Model):
	title = models.CharField(max_length=100)


	def __str__(self):
		return self.title



class ChatRoomMessage(models.Model):
	writer = models.CharField(max_length=255)
	message = models.CharField(max_length=5000, verbose_name="Leave a Comment")
	room = models.ForeignKey(ChatRoom, related_name='chatMessages', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, auto_now =False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return str(self.room)

	class Meta:
		ordering = ['-updated','-created']