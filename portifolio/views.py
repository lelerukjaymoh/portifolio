from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_post(request, pk):
    return render(request, 'details.html', {})

def projects(request, pk):
    return render(request, 'details.html', {})

def project_details(request, pk):
    return render(request, 'details.html', {})
