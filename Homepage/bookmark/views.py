from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from bookmark.models import Bookmark

# from Homepage.views import LoginRequiredMixin 
from django.urls import reverse_lazy 

# Create your views here.

class BookmarkLV(ListView): 
    templates_name = "bookmark_list.html"
    model=Bookmark


class BookmarkDV(DetailView): 
    template_name="bookmark_detail.html"
    model = Bookmark

# class BookmarkCreateView(LoginRequiredMixin,CreateView):

#     model= Bookmark 
