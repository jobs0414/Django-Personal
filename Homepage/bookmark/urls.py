from django.urls import path 
from django.conf.urls import url
from bookmark.views import *

app_name='bookmark'

urlpatterns = [
    
    path('',BookmarkLV.as_view(),name='index'), 
    path('<int:pk>',BookmarkDV.as_view(),name='detail'),
    

]
