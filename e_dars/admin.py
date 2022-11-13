from django.contrib import admin
from .models import *


# class ScinceAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug_name': ('name',)}


# class ThemeAdmin(admin.ModelAdmin):
#     list_display = ['scince', 'theme']


# class QuizesAdmin(admin.ModelAdmin):
#     list_display = ['question', 'ball', 'timer']


# class PractisThemeAdmin(admin.ModelAdmin):
#     list_display = ['scince', 'practis_name', 'practis_id']
#     prepopulated_fields = {'practis_slug': ('practis_name',)}


# class GlossaryAdmin(admin.ModelAdmin):
#     list_display = ['name']


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'post_views', 'created_at']


# class ResourceCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']


# class ResourceAdmin(admin.ModelAdmin):
#     list_display = ['resource', 'name']


# admin.site.register(Scince, ScinceAdmin)
# admin.site.register(Theme, ThemeAdmin)
# admin.site.register(Quizes, QuizesAdmin)
# admin.site.register(Practis)
# admin.site.register(PractisTheme, PractisThemeAdmin)
# admin.site.register(Glossary, GlossaryAdmin)
# admin.site.register(Post, PostAdmin)
# admin.site.register(ResourceCategory, ResourceCategoryAdmin)
# admin.site.register(Resource, ResourceAdmin)
# admin.site.register(Video)
