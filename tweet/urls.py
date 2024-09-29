from django.urls import path
from . import views

urlpatterns = [
 
 path("",views.tweets_list,name='tweets_list'),
 path("create/",views.tweets_create,name='tweets_create'),
 path("<int:tweet_id>/edit/",views.tweets_edit,name='tweets_edit'),
 path("<int:tweet_id>/delete/",views.tweets_delete,name='tweets_delete'),
 path("register/",views.register,name='register'),
 
 
 
 

]

