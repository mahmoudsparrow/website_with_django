from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import RegistarionForm, EditProfileForm, EditUserInfo, LoginForm
from django.contrib.auth import update_session_auth_hash, login, logout, authenticate

from django.views.generic import TemplateView


# Create your views here.
class homeView(TemplateView):
    # template_name = 'home/home.html'
    def get(self, request):
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
        return render(request, 'home/home.html', data)
        # template_name = 'home/home.html'


