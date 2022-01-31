from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from . forms import RoomForm, ChatMessageForm
from . models import ChatRoom, ChatRoomMessage


def index(request):
	form = RoomForm()

	if request.method == "POST":
		form = RoomForm(request.POST)
		if form.is_valid():
			print('form valid')
			render(request, 'chat/index.html', {'form':RoomForm(request.POST)})
	context = {'form':form}
	return render(request, 'chat/index.html',context)


def chatRoom(request,roomName,username):

	room = ChatRoom.objects.get(title=roomName)
	form = ChatMessageForm()

	context = {'room':room, 'form':form,'username':username}

	return render(request,'chat/room.html',context)


def chatRoomProcessor(request):

	title = request.POST['room_name']
	username = request.POST['username']

	if ChatRoom.objects.filter(title=title).exists():
		return redirect ('chatRoom', title, username)
	else:
		newRoom = ChatRoom.objects.create(title=title)
		newRoom.save()
		return redirect('chatRoom',newRoom.title,username)

def sendMessage(request):
	if request.method == "POST":
		try:
			message = request.POST['message']
			username = request.POST['username']
			roomID = request.POST['roomID']
			room = ChatRoom.objects.get(pk=roomID)
			newMessage = ChatRoomMessage.objects.create(message=message, writer=username, room=room)
			newMessage.save()
			return HttpResponse('Message Sent')
		except Exception as e:
			print(e)
			return HttpResponse('Something went wrong ')

def messageLoader(request,roomID):
	room = ChatRoom.objects.get(pk=roomID)

	messages = ChatRoomMessage.objects.filter(room=room)
	
	return JsonResponse({"messages":list(messages.values())})



