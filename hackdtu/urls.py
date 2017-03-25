"""hackdtu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app_views.index, name="index"),
    url(r'^login/$', app_views.login_page, name="login"),
    url(r'^signup/$', app_views.signup_page, name="signup"),
    url(r'^main/(\w+)/$', app_views.main_page, name="main"),
    url(r'^logout/$', app_views.logout_page, name="logout"),
    url(r'^BMR/', include('BMR.urls')),
]
