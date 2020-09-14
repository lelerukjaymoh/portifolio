from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portifolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('blog/posts/page-<int:page>', views.blog_list, name='blog_list'),
    path('blog/post/<slug:slug>', views.blog_post, name='blog_post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
