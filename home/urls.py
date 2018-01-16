from django.conf.urls import url
# from home import views
from home.views import homeView


urlpatterns = [
    url(r'^$', homeView.as_view(), name='home'),
]