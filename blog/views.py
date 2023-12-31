from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request):
    contexto = {
        "text": "Estamos no blog",
        "title": "Blog - ",
        "posts": posts,
    }
    return render(request, "blog/index.html", contexto)


def post(request, post_id):
    found_post = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break
    contexto = {
        "text": "Estamos no blog",
        "title": "Blog - ",
        "post": found_post,
    }
    return render(request, "blog/post.html", contexto)


def exemplo(request):
    print("exemplo")
    contexto = {
        "text": "Estamos no exemplo do blog",
        "title": "Exemplo - ",
    }

    return render(request, "blog/exemplo.html", contexto)
