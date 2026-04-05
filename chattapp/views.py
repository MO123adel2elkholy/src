from django.shortcuts import render, redirect
from . import forms
from .models import Profile, Friend, ChattMessage
# Create your views here.


def index(request):
    user = request.user.profile
    friends = user.friends.all()
    data = {'user': user, 'friends': friends}
    return render(request, 'index.html', data)


def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    form = forms.ChattMessageForm()
    chatts = ChattMessage.objects.all()
    if request.method == 'POST':
        form = forms.ChattMessageForm(request.POST)
        if form.is_valid():
            chatt_messages = form.save(commit=False)
            chatt_messages.sender = user
            chatt_messages.reciver = profile
            chatt_messages.save()
            return redirect('detail', pk=friend.profile.id)

    return render(request, 'detail.html', {"friend": friend, 'form': form, 'user': user, 'profile': profile, 'chatts': chatts})
