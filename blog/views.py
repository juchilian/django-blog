from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost

def home_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)

def blog_post_detail_page(request, slug):
    # qs = BlogPost.objects.filter(slug=slug)
    # post = qs.first()
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"post": post}
    return render(request, 'blog/blog_post_detail.html', context)