from django.conf.urls import url
from .views import index,list,detail

urlpatterns = [
    url(r'^index/$',index),
    url('^list/$',list),
    url(r'^detail/(\d+)/$',detail),
]