from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html' # passing object_list build in to template


class BlogDetailView(DetailView):
    model = Post  # by default it provide a context object we can use in our template called object or post(lower case of model name)
    template_name = 'post_detail.html' # detailview expects either primary key or slug to it as a identifier
    # if you set a context object name then sent it to the html file
    # context_object_name = 'my_object' # here you can create context object name is my_object,rahter than build in context object name is object or post(lowercase model name),



