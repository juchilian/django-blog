from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

def home_view(request):
    posts = BlogPost.objects.published()[:5]
    context = {"title":"Welcome to DJ BLog!!", "posts": posts}
    return render(request, 'home.html', context)

def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    context = {"title":"All Blog Posts", 'posts': qs}
    template_name = 'blog/list.html'
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create obj
    # use a form
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    context = {'form': form}
    template_name = 'blog/form.html'
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"post": post}   
    template_name = 'blog/detail.html'
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
    context = {"title": f"Update {post.title}", 'form': form}
    template_name = 'blog/form.html'
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        post.delete()
        return redirect("/blog")
    context = {'post': post}
    return render(request, template_name, context)