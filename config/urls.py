from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from kafedra.views import edars_detail
from django.conf.urls import handler404, handler500 
from kafedra.views import error_404_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lk/', include('teachers.urls')),
    path('e-darslik/', include('e_dars.urls')),
    path('e-darslik/<slug:slug>', edars_detail, name='edarslik'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('kafedra.urls')),
    path('error/', error_404_view, name='error_404'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]


handler404 = "kafedra.views.error_404_view"