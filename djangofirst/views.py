from django.shortcuts import render, HttpResponse
from accounts.forms import RegistarionForm, LoginForm
from django.contrib.auth import login, logout, authenticate


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
