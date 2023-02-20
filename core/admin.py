from django.contrib import admin
from core import models as core_models

@admin.register(core_models.Categorie)
class Catetegorie(admin.ModelAdmin):
    list_filter = ('name','id')
    search_fields = ('name', 'description')

@admin.register(core_models.Posts)
class Post(admin.ModelAdmin):
    list_filter = ('date',)
    readonly_fields = ('comments',)
    search_fields = ('titre', 'description', 'body')

@admin.register(core_models.Commentaires)
class Commentaire(admin.ModelAdmin):
    readonly_fields = ('adresse', 'commentaire', 'post')
    list_filter = ('post', 'date')

@admin.register(core_models.Email)
class Email(admin.ModelAdmin):
    list_filter = ('date',)
    search_fields =('email',)
