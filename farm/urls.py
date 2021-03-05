from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('news',views.news,name="news"),
    path('dealer',views.dealer,name="dealer"),
    path('profile',views.profile,name="profile"),
    path('shop',views.shop,name="shop"),
    path('signup',views.signup,name="signup"),
    path('register',views.register,name="register"),
    path('enter',views.enter,name="enter"),
    path('logout',views.logout,name='logout'),
    path('edit',views.edit,name="edit")

]