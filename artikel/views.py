from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group

from django.db.models import Count

from artikel.models import Kategori, ArtikelBlog
from artikel.forms import KategoriForm, ArtikelForm, UserEditForm
from django.shortcuts import get_object_or_404

# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user > 0:
        return True
    else:
        return False 
    
####################### USER ########################
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = ArtikelBlog.objects.filter(created_by=request.user)
    context = {
        "artikel":artikel,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/pengguna/artikel_form.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(artikel_list)
        
    forms = ArtikelForm()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/pengguna/artikel_form.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.error(request, "Halaman yang diminta tidak ditemukan!")
        return redirect("dashboard")
    
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan update artikel.')
            return redirect(artikel_list)
        
    forms = ArtikelForm(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, "Artikel berhasil dihapus.")
    except:
        messages.error(request, "Artikel gagal dihapus.")
    return redirect('artikel_list')


####################### ADMIN ########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_form.html"
    if request.method == "POST":
        forms = KategoriForm(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Kategori berhasil ditambahkan.")
            return redirect(admin_kategori_list)
        
    forms = KategoriForm()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_form.html"
    kategori = Kategori.objects.get(id=id_kategori)
    
    if request.method == "POST":
        forms = KategoriForm(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Kategori berhasil diperbarui.")
            return redirect(admin_kategori_list)
        
    forms = KategoriForm(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, "kategori berhasil dihapus.")
    except:
        messages.error(request, "kategori gagal dihapus.")
    return redirect('admin_kategori_list')

####################### ARTIKEL BLOG ########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_form.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_artikel_list)
        
    forms = ArtikelForm()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_form.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)
    
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan update artikel.')
            return redirect('admin_artikel_list')
        
    forms = ArtikelForm(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, "Artikel berhasil dihapus.")
    except:
        messages.error(request, "Artikel gagal dihapus.")
    return redirect('admin_artikel_list')

####################### Manajemen User Oleh Admin as Operator ########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user
    }
    return render(request, template_name, context)

@login_required(login_url='login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = "dashboard/admin/user_edit.html"
    user = get_object_or_404(User, pk=user_id)  # Ambil objek user berdasarkan ID, atau 404 jika tidak ditemukan
    all_groups = Group.objects.all()
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_staff = request.POST.get('is_staff')
        groups_checked = request.POST.getlist('groups')
       
        if not last_name:  # Jika last_name kosong
            messages.error(request, "Nama belakang tidak boleh kosong.")
            return redirect('admin_management_user_edit', user_id=user.id)
        
        if is_staff == None:
            is_staff = False
        else:
            is_staff = True

        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f'Berhasil Melakukan Update Untuk User {user.username}')
        return redirect(admin_management_user_list)  # Redirect ke halaman daftar user setelah berhasil
    else:
        forms = UserEditForm(instance=user)  # Isi form dengan data user yang sudah ada (untuk tampilan awal)
    context = {
        'user':user,
        'all_groups':all_groups,
        'group_user':group_user,
        'forms':forms,
    }
    return render(request, template_name, context)

