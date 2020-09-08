from django.shortcuts import render
from django.http import Http404
from django.conf import settings

from butter_cms import ButterCMS
from datetime import datetime
import pprint

client = ButterCMS(settings.BUTTER_CMS_KEY)

def home(request):
    return render(request, 'index.html', {})

def blog(request):
    response = client.posts.all({'page_size': 1,})    
    pprint.pprint(response)

    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    context = {
        'recent_posts': recent_posts,
    }
    return render(request, 'blog.html', context)

def blog_list(request, page):
    response = client.posts.all({'page_size': 1, 'page': page})
    pprint.pprint(response)

    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']

    context = {
        'recent_posts': recent_posts,
        'next_page': next_page,
        'previous_page': previous_page
    }
    return render(request, 'blog-list.html', context)

def blog_post(request, slug):
    try:
        response = client.posts.get(slug)
    except:
        raise Http404('Post not found')

    post = response['data']
    pprint.pprint(post)
    return render(request, 'blog-post.html', {
        'post': post
    })

def projects(request, pk):
    return render(request, 'details.html', {})

def project_details(request, pk):
    return render(request, 'details.html', {})
