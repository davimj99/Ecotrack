from django.urls import path
from . import views
from monitoramento import views as monitoramento_views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path('postagens/', views.lista_postagens, name='lista_postagens'),
    path('monitoramento/', views.monitoramento_view, name='monitoramento'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('mudas/', views.total_mudas, name='total_mudas'),
    path('api/areas/', monitoramento_views.areas_json, name='areas_json'),

]
