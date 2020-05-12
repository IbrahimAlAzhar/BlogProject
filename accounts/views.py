from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    # you can also create custom class without using it
    form_class = UserCreationForm  # build in django creation form (for sign up),you don't need to create a form
    # in generic class based view the urls are not loaded when the file is imported,so we use lazy form of reverse
    success_url = reverse_lazy('login') # after sign up then redirect login
    template_name = 'signup.html'


