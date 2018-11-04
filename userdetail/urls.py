from django.urls import include, path
from django.contrib.auth import views as auth_views

from .views import SettingsView


app_name = 'userdetail'


urlpatterns = [
    path('userdetail/', include(([
        path('settings/', SettingsView.as_view(), name='settings'),
    ]))),
]


