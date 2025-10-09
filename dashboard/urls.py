from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path('postagens/', views.lista_postagens, name='lista_postagens'),
    path('monitoramento/', views.monitoramento_view, name='monitoramento'),
    
]
