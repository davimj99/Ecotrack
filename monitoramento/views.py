from django.http import JsonResponse
from .models import Area

def areas_json(request):
    areas = Area.objects.all()
    data = [
        {
            'id': area.id,
            'lat': float(area.latitude),
            'lng': float(area.longitude),
            'status': area.status,
            'title': area.nome,
            'problem': area.problema if area.problema else '',  # evita undefined
            'image': area.imagem.url if area.imagem else '',     # pega URL da imagem
            'last': area.criado_em.strftime('%d/%m/%Y')
        }
        for area in areas
    ]
    return JsonResponse(data, safe=False)
