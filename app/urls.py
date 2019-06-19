from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.home,name = 'homePage'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
]