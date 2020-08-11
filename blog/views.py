from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.generic import DetailView
from blog.models import Post

class PostDetailView(DetailView):
    model = Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})