from django.urls import path
from artikel.api import (
    api_artikel_blog_list,
    api_artikel_blog_tambah,
    api_artikel_blog_update,
    api_artikel_blog_delete,

    api_kategori_counts
)
urlpatterns = [
    ####################### FUNGSI-API ########################
    path('artikel/list', api_artikel_blog_list),
    path('artikel/tambah', api_artikel_blog_tambah),
    path('artikel/update/<int:id_artikel>', api_artikel_blog_update),
    path('artikel/delete/<int:id_artikel>', api_artikel_blog_delete),

     path('kategori/counts', api_kategori_counts),
]


