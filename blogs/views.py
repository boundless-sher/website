from django.shortcuts import render
from .models import Post 

# Create your views here.
def blogs_list(request):
    blogs = Post.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs_list.html', context)

def hx_blogs_list(request):
    tag=request.GET.get("filter")
    if tag == None:
        blogs = Post.objects.all()
    else: 
        blogs = Post.objects.filter(tag=tag).all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/responses/filter_page.html', context)


def blog_detail(request, blog_slug):
    blog = Post.objects.filter(slug=blog_slug).first() # so you get None if wrong slug
    if(blog == None):
      return blog_notfound(request, blog_slug)

    context = {
        'blog': blog,
        'word_count': len(blog.body.split())
    }
    return render(request, 'blogs/blog_detail.html', context)

def blog_notfound(request, title):
    return render(request, 'blogs/blog_notfound.html', {'title': title})