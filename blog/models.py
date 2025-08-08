from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Autores"


class Postagem(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.data}"

    class Meta:
        verbose_name_plural = "Postagens"

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    copyright = models.CharField(max_length=50)
    banner = models.ImageField(upload_to="banner/")
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    x = models.URLField(blank=True)