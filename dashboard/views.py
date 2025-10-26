from django.shortcuts import render, get_object_or_404
from monitoramento.models import Area
from reflorestamento.models import Muda
from comunicacao.models import Post

def index(request):
    total_areas = Area.objects.count()
    total_mudas = sum(m.quantidade for m in Muda.objects.all())
    total_posts = Post.objects.count()

    context = {
        "total_areas": total_areas,
        "total_mudas": total_mudas,
        "total_posts": total_posts,
    }
    return render(request, "dashboard/index.html", context)

def monitoramento_view(request):
    return render(request, 'dashboard/monitoramento.html')

def lista_postagens(request):
    # Ordena pelo campo correto
    posts = Post.objects.all().order_by('-publicado_em')
    return render(request, 'dashboard/postagens.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'dashboard/post_detail.html', {'post': post})

def total_mudas(request):
    total = sum(m.quantidade for m in Muda.objects.all())
    return render(request, 'dashboard/total_mudas.html', {'total': total})
