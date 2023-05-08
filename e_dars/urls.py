from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.home_page, name='home'),

    path('<slug:slug>/themes/', views.themes_page, name='themes'),
    path('<slug:slug1>/theme_detail/<slug:slug>/', views.theme_detail, name='theme_detail'),

    path('<slug:slug>/virtuale/', views.virtual_themes_page, name='virtuale'),
    path('<slug:slug1>/virtual_detail/<int:pk>/', views.virtual_page, name='virtual_detail'),

    path('<slug:slug>/video_page/', views.video_page, name='video_page'),

    path('<slug:slug>/resources_page/', views.resources_page, name='resources_page'),

    path('<slug:slug>/glossary_page/', views.glossary_page, name='glossary_page'),

    path('<slug:slug>/practis_themes_page/', views.practis_themes_page, name='practis_themes_page'),
    path('<slug:slug1>/practis_page/<slug:slug>/', views.practis_page, name='practis_page'),

    path('<slug:slug>/quiz_page/', views.quiz_page, name='quiz_page'),

    path('<slug:slug>/quiz_api/', views.quiz_api, name='quiz_api'),

    path('<slug:slug>/sign_up/', views.sign_up, name='sign_up'),
    path('<slug:slug>/sign_in/', views.sign_in, name='sign_in'),
    path('<slug:slug>/logout/', views.logout_user, name='logout'),

    path('pdf/', views.pdf_page, name='pdf'),

]
