from django.http import HttpResponse
from django.shortcuts import render
from Wordplease.models import Post
from Wordplease.models import User
from Wordplease.models import Blog

# Create your views here.

def post_list(request):
    """
    Recupera todas los post de la base de datos
    :param request: HTTP REQUEST
    :return: HTTP RESPONSE
    """
    # Recuperar todas las tareas de la base de datos
    posts = Post.objects.all()

    # Devolver la respuesta
    context = {
        'post_objects': posts
    }
    return render(request, "Wordplease/list.html", context)

def blog_list(request):
    """
        Recupera todas los post de la base de datos
        :param request: HTTP REQUEST
        :return: HTTP RESPONSE
        """
    # Recuperar todas las tareas de la base de datos
    blogs = Blog.objects.all()

    # Devolver la respuesta
    context = {
        'blog_objects': blogs
    }
    return render(request, "Wordplease/blog_list.html", context)