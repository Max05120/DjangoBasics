"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth import views as a
from basics import views
from basics import views as c
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^home/$', c.home, name='home'),
    url(r'^login/$', a.LoginView.as_view(template_name="registration/login.html"),
        name='login'),
    url(r'^login/profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.logoutuser,
        name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
