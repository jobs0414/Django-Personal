from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from bookmark.models import Bookmark

# from Homepage.views import LoginRequiredMixin 
from django.urls import reverse_lazy 
from MyHomepage.views import LoginRequiredMixin
# Create your views here.



class BookmarkLV(ListView): 
    template_name = "bookmark/bookmark_list.html"
    model=Bookmark


class BookmarkDV(DetailView): 
    template_name="bookmark/bookmark_detail.html"
    model = Bookmark
    

class BookmarkCreateView(LoginRequiredMixin,CreateView):

    template_name='bookmark/bookmark_add.html'
    model= Bookmark 
    fields = ['title','url','url_category']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self,form): 
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin,ListView): 
    template_name= "bookmark/bookmark_change_list.html"

    def get_queryset(self):  #전체 리스트 x 필터링 
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin,UpdateView): 

    model =Bookmark 
    fields = ['title','url','url_category']
    success_url = reverse_lazy("bookmark:index")

class BookmarkDeleteView(LoginRequiredMixin,DeleteView):

    model = Bookmark 
    success_url = reverse_lazy('bookmark:index')
