"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # in template we can use login,logout link (django build in),you don't need to create those url
    path('accounts/', include('django.contrib.auth.urls')), # by default login,logout authentication,you can also add
    # accounts/login is use for login in here ," auth_views.LoginView.as_view() " in app url
    path('accounts/', include('accounts.urls')), # to add this url for sign up process, login,logout are automatically handle by django
    # when request accounts/signup url,django will first look in auth not find it then proceed to the accounts app
]
