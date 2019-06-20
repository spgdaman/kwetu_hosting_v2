from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'homePage'),
    path('home/',views.index, name='index'),
    path('profile/',views.profile,name='profile'),
    path('edit/profile/',views.edit_profile,name='edit_profile'),
    path('asset_upload/', views.video_upload, name="upload_video"),
    path('view_assets/',views.view_assets, name="view_assets"),
]