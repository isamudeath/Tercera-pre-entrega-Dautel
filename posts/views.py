from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from posts.models import Post
from posts.forms import Postform

def posts(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts/posts.html',
        context=contexto,
    )
    return http_response

def create_post(request):
    if request.method == "POST":
        postform = Postform(request.POST)
        if postform.is_valid():
            data = postform.cleaned_data
            print(data)
            titulo = data["titulo"]
            contenido = data["contenido"]
            post = Post(titulo=titulo, contenido=contenido)
            post.save()
            url_success = reverse('Post creado')
            return redirect(url_success)
        else:
            postform = Postform(initial=request.POST)
            http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
            )
            return http_response
    else:
        postform = Postform()
        http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
        )
        return http_response

def post_succ(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts/post-succ.html',
        context=contexto,
    )
    return http_response