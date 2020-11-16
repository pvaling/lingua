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

    participants = [request.user, tutor.user]
    participants = list(set(participants))

    query = ChatRoom.objects.annotate(count=Count('members')).filter(count=len(participants))

    for pk in participants:
        query.filter(members__pk=pk.pk)

    cnt = query.count()

    if not cnt:
        chatroom = ChatRoom()
        chatroom.save()
        chatroom.members.add(request.user, tutor.user)
        chatroom.save()
    else:
        chatroom = query.first()

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES,
                           initial={
                               'author': request.user,
                               'chatroom': chatroom.id
                           })
        if form.is_valid():
            # form.author = request.user
            form.instance.author = request.user
            form.instance.chatroom = chatroom
            form.save()
            return HttpResponseRedirect(reverse('tutors:tutor_chat', kwargs={'tutor_id': tutor_id}))



    msg_form = MessageForm(initial={
        'author': request.user
    })

    context = {
        'chatroom': chatroom,
        'message_form': msg_form,
        'tutor': tutor
    }
    return render(request, 'tutors/chat.html', context=context)
