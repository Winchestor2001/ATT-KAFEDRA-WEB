from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name='home'),
    path('teachers/', views.teachers_page, name='teachers'),
    path('teacher_portfolio/<int:pk>', views.teacher_portfolio_page, name='teacher_portfolio'),
    path('edars/', views.edars_page, name='edars'),
    path('edars/<slug:slug>/', views.edars_detail, name='edars_detail'),
    path('subjects/', views.subjects_page, name='subjects'),
    path('tarixi/', views.tarixi_page, name='tarixi'),
    path('contact/', views.contact_page, name='contact'),
    path('articles/<int:article_type>/', views.articles, name='articles'),
    path('best_students/', views.best_students_page, name='best_students'),
    path('teacher_portfolio/teacher_portfolio_ajax/', views.teacher_portfolio_ajax, name='teacher_portfolio_ajax'),

    path('article_detail/<slug:slug>/', views.article_detail, name='article_detail'),
]