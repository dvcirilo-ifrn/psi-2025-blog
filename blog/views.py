from django.shortcuts import render
from .models import Postagem, Blog

postagens = [
    {
        "id": 1,
        "titulo": "Minha primeira postagem",
        "subtitulo": "Nessa postagem o conteúdo é muito importante",
        "autor": "James Wilson",
        "data": "27 de junho de 2025",
        "conteudo": '<p class="teste">Lorem ipsum dolor sit amet</p>, consectetur adipiscing elit. Phasellus tempus volutpat turpis ut placerat. Cras vitae tristique est, non pellentesque eros. Pellentesque pretium elit sed turpis aliquam efficitur. Aenean sit amet magna a nunc condimentum consequat. <br> Suspendisse potenti. Morbi luctus neque sed libero tristique, sit amet porta eros tempus. Integer a vulputate leo. Cras quis diam imperdiet, bibendum purus vel, posuere dui. Proin in nisi arcu. Morbi id diam ut urna bibendum ornare. Duis interdum nunc ut dolor posuere rhoncus. Phasellus tincidunt egestas vulputate.',
        "imagem": "blog/img/post-bg.jpg",
    },
    {
        "id": 2,
        "titulo": "Minha segunda postagem",
        "subtitulo": "Nessa postagem o conteúdo é muito mais importante",
        "autor": "Peter Wilson",
        "data": "1 de julho de 2025",
        "conteudo": "Conteúdo super interessante da minha postagem",
        "imagem": "blog/img/3409297.jpg",
    },
    {
        "id": 3,
        "titulo": "Minha third postagem",
        "subtitulo": "Nessa post o content é muito more importante",
        "autor": "Jane Sebastian",
        "data": "10 de julho de 2025",
        "conteudo": "Conteúdo super interessante da minha postagem",
        "imagem": "post-bg.jpg",
    },
]

def index(request):
    context = {
        "postagens": Postagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/index.html", context)

def sobre(request):
    return render(request, "blog/sobre.html")

def post(request, id_post):
    return render(request, "blog/post.html", postagens[id_post-1])

def contato(request):
    return render(request, "blog/contato.html")