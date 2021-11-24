from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
    ordering =  ['site_name']

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']   # Bookmark 테이블에서 연결할 Field 목록
    success_url = reverse_lazy('list') # 작업 완료 후 연결 link name
    template_name_suffix = '_create'  #  모델클래스_create.html 와 연결

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')



