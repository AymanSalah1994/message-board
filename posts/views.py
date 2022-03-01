from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'posts/home.html'
    # Notice that , HOmePageView will Inherit from List View
    #  And Hence it will Return Object_list
    # Which is The Context
    # context_object_name =  We will test this Vairalbe later  ;
    context_object_name = 'The_sent_context'
