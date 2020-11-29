from django.db.models import Count
from django.forms import ModelForm, CharField, Textarea
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from tutors.models import Tutor, ChatRoom, ChatMessage


class MessageForm(ModelForm):

    body = CharField(widget=Textarea(attrs={'rows': 4}))

    class Meta:
        model = ChatMessage
        fields = ('body',)

def tutor_chat(request, tutor_id):

    tutor = Tutor.objects.get(id=int(tutor_id))

    query = ChatRoom.objects.all().filter(members=tutor.user).filter(members=request.user)

    cnt = query.count()

    if not cnt:
        chatroom = ChatRoom()
        chatroom.save()
        chatroom.members.add(request.user, tutor.user)
        chatroom.save()
    else:
        chatroom = query.first()

    return HttpResponseRedirect(reverse('tutors:chatroom', kwargs={'chatroom_id': chatroom.id}))


def tutor_chatrooms(request):
    context = {
        'chatrooms': ChatRoom.objects.filter(members=request.user)
    }
    return render(request, 'tutors/tutor_chatrooms.html', context=context)


def chatroom(request, chatroom_id):
    #todo: check access!!!

    chatroom = ChatRoom.objects.get(pk=int(chatroom_id))

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES,
                           initial={
                               'author': request.user,
                               'chatroom': chatroom_id
                           })
        if form.is_valid():
            # form.author = request.user
            form.instance.author = request.user
            form.instance.chatroom = chatroom
            form.save()
            return HttpResponseRedirect(reverse('tutors:chatroom', kwargs={'chatroom_id': chatroom_id}))



    msg_form = MessageForm(initial={
        'author': request.user,
    })

    context = {
        'chatroom': chatroom,
        'message_form': msg_form,
    }
    return render(request, 'tutors/chat.html', context=context)
