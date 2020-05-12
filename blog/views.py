from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html' # passing object_list build in to template


class BlogDetailView(DetailView):
    model = Post  # by default it provide a context object we can use in our template called object or post(lower case of model name)
    template_name = 'post_detail.html' # detailview expects either primary key or slug to it as a identifier
    # if you set a context object name then sent it to the html file
    # context_object_name = 'my_object' # here you can create context object name is my_object,rahter than build in context object name is object or post(lowercase model name),


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'  # fields is all attribute of model (title,author)


class BlogUpdateView(UpdateView):
    model = Post # automatically using id as a pk (class based view) and returns to urls file
    fields = ['title','body'] # explicitly listing the fields we want to use rather than using __all__
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home') # after deleting post then redirects to home(url name)
    # reverse_lazy as opposed to just reverse so that it won't execute the URL redirect until out view has finished deleting the blog post
