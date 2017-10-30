from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import blog
from .forms import AddBlogForm


def index(request):
	blogs = blog.objects.all()
	return render(request,'blogapp/index.html',{'blogs':blogs})
# Create your views here.

def detail(request, blog_id):
	detailBlog = get_object_or_404(blog, pk=blog_id)
	return render(request,'blogapp/detail.html',{'detailBlog':detailBlog})

class AddBlog(generic.CreateView):
    form_class = AddBlogForm
    template_name = 'blogapp/add_blog.html'
    success_url = '/'