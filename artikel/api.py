from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from artikel.models import ArtikelBlog, Kategori
from artikel.serializers import ArtikelBlogSerializer
from django.db.models import Count

@api_view(['GET'])
def api_artikel_blog_list(request):
    artikel = ArtikelBlog.objects.all()
    serializer = ArtikelBlogSerializer(artikel, many=True)
    content = {
        "messages":"Berhasil",
        "record":artikel.count(),
        "rows":serializer.data
    }
    return Response(content, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_kategori_counts(request):
    category_data = Kategori.objects.annotate(article_count=Count('artikelblog'))
    data = {kategori.nama: kategori.article_count for kategori in category_data}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_artikel_blog_tambah(request):
    data = request.data.copy()
    # user = User.objects.last()
    # data['created_by'] = user.id

    serializer = ArtikelBlogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "messages":"Artikel Berhasil Ditambahkan",
            "data":serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "messages":"Artikel Gagal Ditambahkan",
            "errors":serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def api_artikel_blog_update(request, id_artikel):
    artikel = get_object_or_404(ArtikelBlog, id=id_artikel)

    data = request.data.copy()
    serializer = ArtikelBlogSerializer(instance=artikel, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "messages":"Artikel Berhasil Diperbarui",
            "data":serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "messages":"Artikel Gagal Diperbarui",
            "errors":serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_artikel_blog_delete(request, id_artikel):
    try:
        artikel = get_object_or_404(ArtikelBlog, id=id_artikel)
        artikel.delete()
        content ={
            "messages":"Artikel Berhasil Dihapus",
        }
        status_code = status.HTTP_200_OK
    except:
        content ={
            "messages":"Artikel Gagal Dihapus",
        }
        status_code = status.HTTP_400_BAD_REQUEST
    return Response(content, status=status_code)