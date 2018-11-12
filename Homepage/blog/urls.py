from django.urls import path 
from django.conf.urls import url 
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('',PostLV.as_view(),name='index'),
    path('post',PostLV.as_view(),name="post_list"),
    path('post',PostDV.as_view(),name='post_detail'),

    path('archive',PostAV.as_view(),name='post_archive'),
    path('<int:year>',PostAV.as_view(),name="post_archive"),
    path('<int:year>/<str:month>',PostMAV.as_view(),name='post)archive'),
    path('<int:year>/<str:month>/<int:day>',PostDAV.as_view(),name="post_day_archive"),

]