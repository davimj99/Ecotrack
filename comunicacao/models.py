from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="posts/imagens/", blank=True, null=True)
    video = models.FileField(upload_to="posts/videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    publicado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
