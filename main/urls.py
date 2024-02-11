from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('discover/',views.discover, name="discover"),
    path('login/',views.ulogin,name="login"),
    path('signup/',views.usignup,name="signup"),
    path('logout/',views.ulogout,name='logout'),
    path('music/',views.music, name="music"),
    path('comics/',views.comics, name='comics'),
    path('novels/',views.novels, name='novels'),

    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('main/songs/<int:id>', views.songpost, name='songpost'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('history', views.history, name='history'),
    path('music/c/<str:channel>', views.channel, name='channel'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
]
