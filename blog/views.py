from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

def home_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'index.html', context)

def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all() # queryset -> list of python object
    context = {'posts': qs}
    template_name = 'blog/list.html'
    return render(request, template_name, context)

# @staff_member_required
@login_required
def blog_post_create_view(request):
    # create obj
    # use a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()

    context = {'form': form}
    template_name = 'blog/create.html'
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"post": post}   
    template_name = 'blog/detail.html'
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {'post': post, 'form': None}
    return render(request, 'update.html', context)

def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {'post': post}
    return render(request, 'delete.html', context)