from django.shortcuts import render


# Create your views here.
def blog(request):
    contexto = {"text": "Estamos no blog", "title": "Blog - "}
    return render(request, "blog/index.html", contexto)


def exemplo(request):
    print("exemplo")
    contexto = {"text": "Estamos no exemplo do blog", "title": "Exemplo - "}

    return render(request, "blog/exemplo.html", contexto)
