from django.contrib import admin
from .models import *


class PhotoAdmin(admin.StackedInline):
    model = PortfolioImage


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_id']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
    prepopulated_fields = {'subject_slug': ('subject_name',)}


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['subject', 'glossary_title']
    prepopulated_fields = {'glossary_slug': ('glossary_title',)}


@admin.register(Maruza)
class MaruzaAdmin(admin.ModelAdmin):
    list_display = ['subject', 'maruza_title']
    prepopulated_fields = {'maruza_slug': ('maruza_title',)}


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['subject', 'question']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['subject', 'video_title']


@admin.register(Virtual)
class VirtualAdmin(admin.ModelAdmin):
    list_display = ['subject', 'virtual_title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['subject', 'book_title']


@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    list_display = ['subject', 'site_title']


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['subject', 'presentation_title']


@admin.register(Amaliy)
class AmaliyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'question_slug': ('question_title',)}
    list_display = ['practis_name', 'question_title']


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'portfolio_slug': ('portfolio_name',)}
    list_display = ['portfolio_name']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['category', 'teacher', 'portfolio_name']
    inlines = [PhotoAdmin]


@admin.register(AmaliyTheme)
class AmaliyThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'practis_slug': ('practis_name',)}
    list_display = ['subject', 'practis_name']


@admin.register(SubjectCategory)
class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(BestStudent)
class BestStudentAdmin(admin.ModelAdmin):
    list_display = ['name']
