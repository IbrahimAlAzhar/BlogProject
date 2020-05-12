from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    # django automatically add pk on database model, detailview expects pk
    #  it expects to be passed an argument pk representing the primary key for the blog post,and pass it from home.html
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'), # detailview expects either primary key or slug to it as a identifier
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]