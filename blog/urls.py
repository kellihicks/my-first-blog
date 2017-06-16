from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^json_all_posts$', views.json_all_posts, name='json_all_posts'),
   url(r'^spa_post_list$', views.spa_post_list, name='spa_post_list'),
   url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
   url(r'^post/new/$', views.post_new, name='post_new'),
   url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), 
]

     
        
