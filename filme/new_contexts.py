from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8] # o - na frente do data_criacao indica ordem decrescente (mais recente primeiro)
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_populares": lista_filmes}


def filme_destaque(request):
    if Filme.objects.all():
        filme = Filme.objects.order_by('-visualizacoes')[0]
    else:
        filme = None
    return {"filme_destaque": filme}







