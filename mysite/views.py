from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    artikel_user = ArtikelBlog.objects.filter(
        created_by=request.user,
        status=True
    ).order_by('-created_at')[:4] 

  
    kategori_counts = {}
    for kategori in Kategori.objects.all():
        count = ArtikelBlog.objects.filter(
            kategori=kategori,
            status=True
        ).count()
        kategori_counts[kategori.nama] = count

    context = {
        "title": "Selamat Datang",
        "artikel_user": artikel_user,
        "kategori_counts": kategori_counts
    }
    return render(request, "dashboard/index.html", context)

@login_required(login_url='login')
def artikel_list(request):
    artikel_user = ArtikelBlog.objects.filter(
        created_by=request.user,
        status=True
    ).order_by('-created_at')

    context = {
        "title": "Daftar Artikel",
        "artikel_user": artikel_user
    }
    return render(request, "dashboard/artikel_list.html", context)