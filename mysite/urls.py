from django.contrib import admin
from django.urls import path, include
# Media #
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from mysite.views import *
from mysite import views
from mysite.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', index),
    path('artikel/<int:id>', views.detail_artikel, name='detail_artikel'),
    path('artikel-not-found', not_found_artikel, name='not_found_artikel'),
    path('kontak/', kontak, name='kontak'),
    path('galeri/', galeri, name='galeri'), 
    path('auth-logout', logout, name='auth-logout'),
    path('auth-registrasi', registrasi, name='registrasi'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Media #

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
