from django import forms
from django.forms import ModelForm
from . models import ChatRoomMessage

class RoomForm(forms.Form):
	username = forms.CharField()
	room_name = forms.CharField(label="Room Name")

class ChatMessageForm(ModelForm):
	class Meta:
		model = ChatRoomMessage
		fields = ['message']