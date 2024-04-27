from django.shortcuts import render
from.models import ChatRoom,ChatMessage
# Create your views here.
def index(request):
    chatRooms=ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatRooms':chatRooms})

def chatroom(request,slug):
    chatRoom=ChatRoom.objects.get(slug=slug)
    messages=ChatMessage.objects.filter(room=chatRoom)[0:30]
    return render(request,'chatapp/room.html',{'chatRoom':chatRoom,'messages':messages})