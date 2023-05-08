from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='lk'),

    path('maruzalar/', views.maruzalar_page, name='maruzalar'),
    path('maruzalar/edit_maruza/', views.edit_maruza, name='edit_maruza'),
    path('delete_maruza/<str:slug>', views.delete_maruza, name='delete_maruza'),
    path('delete_all_maruza/', views.delete_all_maruza, name='delete_all_maruza'),

    path('glossaries/', views.glossary_page, name='glossaries'),
    path('glossaries/edit_glossary/', views.edit_glossary, name='edit_glossary'),
    path('delete_glossary/<str:slug>', views.delete_glossary, name='delete_glossary'),
    path('delete_all_glossary/', views.delete_all_glossary, name='delete_all_glossary'),

    path('amaliy/', views.amaliy_page, name='amaliy'),
    path('amaliy/edit_amaliy/', views.edit_amaliy, name='edit_amaliy'),
    path('amaliy/edit_amaliy2/', views.edit_amaliy2, name='edit_amaliy2'),
    path('delete_amaliy/<str:slug>', views.delete_amaliy, name='delete_amaliy'),
    path('delete_amaliy2/<str:slug>', views.delete_amaliy2, name='delete_amaliy2'),
    path('delete_all_amaliy/', views.delete_all_amaliy, name='delete_all_amaliy'),
    path('delete_all_amaliy2/', views.delete_all_amaliy2, name='delete_all_amaliy2'),
    path('get_amaliy_ajax/', views.get_amaliy_ajax, name='get_amaliy_ajax'),

    path('videolar/', views.videolar_page, name='videolar'),
    path('videolar/edit_videolar/', views.edit_videolar, name='edit_videolar'),
    path('delete_videolar/<int:pk>', views.delete_videolar, name='delete_videolar'),
    path('delete_all_videolar/', views.delete_all_videolar, name='delete_all_videolar'),

    path('tests/', views.test_page, name='tests'),
    path('tests/edit_test/', views.edit_test, name='edit_test'),
    path('delete_test/<int:pk>', views.delete_test, name='delete_test'),
    path('delete_all_tests/', views.delete_all_test, name='delete_all_tests'),

    path('virtual/', views.virtual_page, name='virtual'),
    path('virtual/edit_virtual/', views.edit_virtual, name='edit_virtual'),
    path('delete_virtual/<int:pk>', views.delete_virtual, name='delete_virtual'),
    path('delete_all_virtual/', views.delete_all_virtual, name='delete_all_virtual'),

    path('book', views.book_page, name='book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('delete_all_book/', views.delete_all_book, name='delete_all_book'),

    path('taqdimot', views.taqdimot_page, name='taqdimot'),
    path('edit_taqdimot/', views.edit_taqdimot, name='edit_taqdimot'),
    path('delete_taqdimot/<int:pk>', views.delete_taqdimot, name='delete_taqdimot'),
    path('delete_all_taqdimot/', views.delete_all_taqdimot, name='delete_all_taqdimot'),

    path('site', views.site_page, name='site'),
    path('edit_site/', views.edit_site, name='edit_site'),
    path('delete_site/<int:pk>', views.delete_site, name='delete_site'),
    path('delete_all_site/', views.delete_all_site, name='delete_all_site'),

    path('profile/', views.profile_page, name='profile'),

    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('portfolio/edit_portfolio/', views.edit_portfolio, name='edit_portfolio'),
    path('delete_portfolio/<int:pk>', views.delete_portfolio, name='delete_portfolio'),
    path('delete_all_portfolio/', views.delete_all_portfolio, name='delete_all_portfolio'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('messages/', views.messages_page, name='messages'),
]















