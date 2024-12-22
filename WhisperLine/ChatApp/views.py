from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request, user)
          return redirect('#') # add the url
    else:
        form = UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})

@login_required
def group_list(request):
    groups = GroupChat.objects.filter(members = request.user)
    return render(request,"group_list.html",{"groups": groups})


@login_required
def group_chat_room(request,group_id):
    group = get_object_or_404(GroupChat,id = group_id)
    messages = group.messages.all()
    if request.method =="POST":
        content  = request.POST.get("message")
        if content:
            Message.objects.create(sender=request.user,group=group,content=content)
            return redirect("group_chat_room",group_id=group.id)
    return render(request,"group_chat_room.html",{"group": group,"messages":messages})


@login_required
def private_chat(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by("timestamp")
    if request.method == "POST":
        content = request.POST.get("message")
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect("private_chat", receiver_id=receiver.id)
    return render(request, "chat/private_chat.html", {"receiver": receiver, "messages": messages})