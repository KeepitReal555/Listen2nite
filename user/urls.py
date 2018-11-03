from django.urls import include, path
from django.contrib.auth import views as auth_views

from .views import check_code, UserSignUpView, UserLoginView

app_name = 'user'

urlpatterns = [
    path('user/', include(([
        # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
        path('signup/', UserSignUpView.as_view(), name='signup'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]))),
    path('checkcode/', check_code, name='checkcode'),
]


