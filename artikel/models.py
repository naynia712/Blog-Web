from django.db import models
from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Kategori"

class ArtikelBlog(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200, unique=True)
    konten = CKEditor5Field('Text', config_name='extends')
    gambar = models.ImageField(upload_to="artikel", blank=True, null=True)
    status = models.BooleanField(default=False) #jika true maka akan muncul di artikel depan

    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "2. Artikel Blogs"

