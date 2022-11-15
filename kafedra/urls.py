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
    path('best_students/', views.best_students_page, name='best_students'),
]