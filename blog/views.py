from django.shortcuts import render
from .models import Blog

def allblogs(request):
    blogs=Blog.objects
    return render(request,'allblogs/allblogs.html',{'blogs':blogs})