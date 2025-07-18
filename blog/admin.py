from django.contrib import admin
from .models import Postagem, Autor, Blog

admin.site.register(Postagem)
admin.site.register(Autor)
admin.site.register(Blog)