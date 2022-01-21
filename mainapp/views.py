from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import BlogPost, Tag

ALL_POSTS = [
 {
    'id':0,
    'author': {'username':'will', 'id':'1'},
    'title':'My first blog post',
    'body': 'This is my first post. I hope you like it.',
    'postdate': datetime(2019, 10, 1),
    'get_absolute_url': '/blog/post/0'
 },
 {
    'id':1,
    'author': {'username':'will', 'id':'1'},
    'title':'My second blog post',
    'body': 'I\'ve got tons of these now. This is fun.',
    'postdate': datetime(2019, 10, 2),
    'get_absolute_url': '/blog/post/1'
 },
]

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'mainapp/index.html', {'posts':posts})

def post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    return render(request, 'mainapp/post.html', {'object': post})

# Add a view to show all posts by a given tag.
def tag_posts(request, name):
    name = name.lower()
    title = "Posts about {}".format(name)

    tag = get_object_or_404(Tag, name=name)
    # Get all posts by using this tag.
    posts = BlogPost.objects.filter(tags=tag)

    return render(request, 'mainapp/filtered_post_list.html', {'posts': posts, 'title': title})