# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import User
from django.urls import reverse_lazy


class UserListView(ListView):
    model = User
    template_name = 'home.html'


class UserDetailView(DetailView): 
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'new_user.html'
    fields = ['name', 'birthday', 'gender']

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = ['name', 'birthday', 'gender']

class UserDeleteView(DeleteView): 
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('home')
