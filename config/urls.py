"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include #[MODIFIED] include는 Django의 URL 분리를 위한 도구
from pybo.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/",include('pybo.urls')), #"pybo/"로 시작하는 URL은 모두 pybo/urls.py파일에서 처리하라는 의미
    path("common/", include('common.urls')), #"common/"로 시작하는 URL은 모두 common/urls.py파일에서 처리하라는 의미
    path("", base_views.index, name='index') #"/"로 시작 URL 패턴
]