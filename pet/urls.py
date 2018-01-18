from django.conf.urls import url

from pet import views

urlpatterns = [
    url(r'^pet/list/$', views.pet_list, name='pet_list'),
    url(r'^pet/new/$', views.pet_new, name='pet_new'),
    url(r'^pet/(?P<pet_id>\d+)/$', views.pet_detail, name='pet_detail'),
    # url(r'^$', views.pet_detail, name='pet_detail'),
    url(r'^ajax/petmng/$', views.pet_mng, name='pet_mng'),
]
