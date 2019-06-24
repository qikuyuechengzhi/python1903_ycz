from django.conf.urls import url
from . import views
app_name = 'information'
urlpatterns = [

    url(r'^$',views.MainView.as_view(),name='main'),
    url(r'^nav/$',views.NavView.as_view(),name='nav'),
    url(r'^nav/index/$',views.IndexView.as_view(),name='index'),
    url(r'^nav/form/$',views.FormView.as_view(),name='form'),
    url(r'^nav/table/$',views.TableView.as_view(),name='table'),
    url(r'^login/$',views.LoginView.as_view(),name='login'),
    url(r'^register/$',views.RegisterView.as_view(),name='register'),
]
