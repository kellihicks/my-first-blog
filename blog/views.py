from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import JsonResponse
from django.core import serializers


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def spa_post_list(request):
    return render(request, 'blog/spa_post_list.html', {})

def json_all_posts(request):
    posts = Post.objects.order_by('published_date')
    data = serializers.serialize('json', posts)
    return JsonResponse(data, safe=False)



