from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def index(request):
    kategori_param = request.GET.get('kategori', None)

    if kategori_param:
        artikel = ArtikelBlog.objects.filter(kategori__nama=kategori_param)
    else:
        artikel = ArtikelBlog.objects.all()

    kategori = Kategori.objects.all()

    context = {
        "title": "Selamat Datang",
        "artikel": artikel,
        "kategori": kategori,
    }
    return render(request, "landingpage/index.html", context)

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found_artikel)

    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)

    context = {
        "title":"selamat datang",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "artikel_not_found.html"
    return render(request, template_name)


def kontak(request):
    template_name = "kontak.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def galeri(request):
    template_name = "galeri.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)
#################### Dashboard ######################
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    template_name = "dashboard/base.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def dashboard_index(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')

    artikel_user = ArtikelBlog.objects.filter(created_by=request.user)
    
    context = {
        "artikel_user": artikel_user,
        "title": "Dashboard"
    }
    return render(request, 'dashboard/index.html', context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)