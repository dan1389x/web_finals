from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views #login 
from .views import custom_login
from .views import image_upload_view
from .views import register
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('index/', views.index, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
    path('artists/', views.artists, name='artists'),
    path('gallery/', views.gallery, name='gallery'),
    path('AngeloBronzino/', views.profile_1, name='profile_1'),
    path('JenőGyárfás/', views.profile_2, name='profile_2'),
    path('JanMatejko/', views.profile_3, name='profile_3'),
    path('VanGogh/', views.profile_4, name='profile_4'),
    path('SalvadorDali/', views.profile_5, name='profile_5'),
    path('KorneyChukovsky/', views.profile_6, name='profile_6'),
    path('shinhui/', views.profile_7, name='profile_7'),
    path('westendorp/', views.profile_8, name='profile_8'),
    path('nizovtsev/', views.profile_9, name='profile_9'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    #login
    path('accounts/login/', auth_views.LoginView.as_view(), name='login1'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout2'),
    #make
    path('make-1/', views.make, name='make'),
    path('make-2/', views.name_template, name='name_template'),
    #test url 
    path('test/', views.test, name='test'),
    #upload
    path('upload/', views.image_upload_view, name='image_upload'),
] 