from django.db import models

class Area(models.Model):
    PROBLEMA_CHOICES = [
        ("desmatamento", "Desmatamento"),
        ("queimada", "Queimada"),
        ("seca", "Seca"),
    ]

    STATUS_CHOICES = [
        ("critico", "Crítico"),
        ("recuperacao", "Em Recuperação"),
        ("estavel", "Estável"),
    ]

    nome = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    problema = models.CharField(max_length=20, choices=PROBLEMA_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="critico")
    imagem = models.ImageField(upload_to="areas/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


