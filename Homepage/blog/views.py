from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView,TodayArchiveView,DayArchiveView

from blog.models import Post
# Create your views here.
from django.views.generic.edit import FormView
# from blog.forms import PostSearchForm
from django.db.models import Q

from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from MyHomepage.views import LoginRequiredMixin


# Create your views here.
class PostLV(ListView): 
    model = Post 
    template_name = 'post_all.html'
    context_object_name = 'posts'
    paginate_by = 4 
    
class PostDV(DetailView): 
    model = Post 

class PostAV(ArchiveIndexView):
    model = Post 
    data_field = 'modify_date'

class PostYAV(YearArchiveView): 
    model = Post 
    data_field = "modify_date"

class PostMAV(MonthArchiveView): 
    model =Post 
    data_field= 'modify_date'

class PostDAV(DayArchiveView): 
    model =Post 
    data_field = "modify_date"

class PostTAV(TodayArchiveView): 
    model =Post 
    data_field = "modify_date"


