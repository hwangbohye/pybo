from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정 필요 없음 
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), 
    path('logout/', views.logout_view , name='logout'),
    path('signup/', views.signup, name='signup'),
]