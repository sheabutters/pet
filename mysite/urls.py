"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from mysite import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^', include('pet.urls', namespace='pet')),
    # list - pet의 목록
    # detail - pet의 id를 가지고 정보를 가져온다.
    # ajax를 통해 값을 주소 받는다.
    url(r'^admin/', admin.site.urls),
]
