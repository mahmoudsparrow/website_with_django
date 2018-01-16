"""
    view of account
"""

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db.models import Q
from accounts.forms import RegistarionForm, EditProfileForm, EditUserInfo, LoginForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from accounts.models import UserProfile, Chat
from home.models import Friend
from django.contrib.auth import update_session_auth_hash, login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
# def loginme(request):
#     return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistarionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:account'))
    else:
        form = RegistarionForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = "SpaRRoW"
    form = RegistarionForm()
    logForm = LoginForm()
    if request.method == 'POST':
        logForm = LoginForm(request.POST or None)
        if logForm.is_valid():
            logout(request)
            username = password = ''
            if request.POST:
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
    # args = {'form': form}
    data = {'name': name, 'numbers': numbers, 'form': form, 'logForm': logForm}
    return render(request, 'accounts/home.html', data)


def profile(request, pk=None):
    form = EditUserInfo(request.POST or None)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        
        if form.is_valid():
            # userProfile = UserProfile(
            #     user_id = request.user.id,
            #     description = form.cleaned_data['description'],
            #     city = form.cleaned_data['city'],
            #     phone = form.cleaned_data['phone'],
            #     websity = form.cleaned_data['websity']
            #     )
            # userProfile = UserProfile.objects.all()
            userProfile = UserProfile.objects.get(pk=request.user.id)
            userProfile.description = form.cleaned_data['description']
            userProfile.city = form.cleaned_data['city']
            userProfile.phone = form.cleaned_data['phone']
            userProfile.websity = form.cleaned_data['websity']
            userProfile.save()
        user = request.user
    users = User.objects.exclude(id=request.user.id)
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        no_of_friends = friends.count()
    except:
        friends = None
        no_of_friends = 0

    args = {'user': user, 'form': form, 'users': users, 'friends': friends, 'no_of_friends': no_of_friends}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:profile'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

def friendship(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.add_friend(request.user, new_friend)
        print(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
        print(request.user, new_friend)
    return redirect(reverse('home:home'))

def messages(request, pk=None):
    pk=pk
    if request.method == 'GET':
        print(request.user.id, pk)
        # chat = Chat.objects.raw('SELECT * FROM `accounts_chat` WHERE (user_id="request.user" OR to_user=request.user) AND (user_id=pk OR to_user=pk)')
        chat = Chat.objects.filter( (Q(user=request.user.id) | Q(to_user=request.user.id)) , (Q(user=pk) | Q(to_user=pk)))
        # if not chat:
        #     chat = Chat.objects.filter(user=pk, to_user=request.user.id)
        args = {'chat': chat, 'pk': pk}
        return render(request, 'accounts/messages.html', args)
    else:
        msg = request.POST.get('chat-msg', None)
        c = Chat(user=request.user, to_user=pk, message=msg)
        if msg != '':
            c.save()
        args = {'msg': msg, 'user': request.user, 'pk': pk}
        return redirect('accounts:messages', pk=pk)
