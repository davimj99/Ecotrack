from django.contrib import admin
from .models import Post


admin.site.site_header = "Administração do ECOTRACK"
admin.site.site_title = "Administração do ECOTRACK"
admin.site.index_title = "Painel Administrativo"

admin.site.register(Post)
