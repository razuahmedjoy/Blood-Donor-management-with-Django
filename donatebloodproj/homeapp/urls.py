
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-donors/', views.alldonors, name='alldonors'),
    path('register/', views.register, name='register'),
    path('createaccount/', views.create_account, name='create_account'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='donorupdate'),


    path('shururkotha/', views.shurur_kotha, name='shurur_kotha'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('mentors/', views.mentors, name='mentors'),
    path('advisers/', views.advisers, name='advisers'),
    path('blogs/', views.blog_home, name='blogs'),
    path('shohojogi/', views.shohojogiview, name='shohojogi'),


    # api calls
    path('requestblood', views.request_blood, name='request_blood'),

]
