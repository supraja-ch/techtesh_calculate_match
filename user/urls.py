from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'user'


urlpatterns = [
    path('home',views.index,name="home"),
    path('user/sign_up/',views.sign_up,name="sign-up")
]