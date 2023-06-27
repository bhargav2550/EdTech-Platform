from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.urls import path,include
from . import settings
from Hack import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.user_login),
    path('regi/',views.regist),
    path('create/',views.createhackathon),
    path('getlist/',views.gethackathons),
    path("accounts/",include('django.contrib.auth.urls')),
    path("logout/",views.logout)
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
