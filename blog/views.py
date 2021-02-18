from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def home_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)

def blog_post_detail_page(request, blog_id):
    try:
        post = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    context = {"post": post}
    return render(request, 'blog/blog_post_detail.html', context)