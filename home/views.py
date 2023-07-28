from django.shortcuts import render


# Create your views here.


def home(request):
    print("home")
    contexto = {"text": "Estamos na home", "title": "Home - "}
    return render(request, "home/index.html", contexto)
