from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('room/<str:roomName>/<str:username>/', views.chatRoom, name='chatRoom'),
	path('processor/',views.chatRoomProcessor,name='findRoom'),
	path('send/', views.sendMessage, name='send'),
	path('messageLoader/<int:roomID>/',views.messageLoader, name='messageLoader')
]