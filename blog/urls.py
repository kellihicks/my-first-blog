from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),url(r'^json_all_posts$', views.json_all_posts, name='json_all_posts'),
 url(r'^spa_post_list$', views.spa_post_list, name='spa_post_list'),
]
 
   
