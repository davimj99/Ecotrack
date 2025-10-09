from django.db import models

class Muda(models.Model):
    especie = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    local = models.CharField(max_length=150)
    responsavel = models.CharField(max_length=100)
    data_plantio = models.DateField()
    observacoes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to="mudas/", blank=True, null=True)

    def __str__(self):
        return f"{self.especie} - {self.local}"

class Animal(models.Model):
    especie = models.CharField(max_length=70)
    foto = models.ImageField(upload_to="animais/", blank=True, null=True)
    origem = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.especie}, {self.origem}"

class Vegetacao(models.Model):
    tipo = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.vegetecao}"

class TipoPlanta(models.Model):
    tipo = models.CharField(max_length=70)
    adubo = models.CharField(max_length=70)
    hora = models.DataField
    

