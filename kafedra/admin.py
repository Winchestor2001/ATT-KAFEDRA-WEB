from django.contrib import admin
from .models import *


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleGalleryAdmin(admin.StackedInline):
    model = ArticleGallery
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'views', 'created_date']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleGalleryAdmin]


admin.site.register(KafedraHistory)
admin.site.register(IqdidorliStudents)

