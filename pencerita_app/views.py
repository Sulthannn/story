from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registrasi(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Berhasil Dibuat!")
            return redirect('registrasi')
        else:
            messages.error(request, "Gagal Dibuat!")
            return redirect('registrasi')
    else:
        form = UserCreationForm()
        data = {
            'Title' : "Daftar - Story.La",
            'form':form,
        }
    return render(request, 'registrasi.html', data)

def index(request):
    if request.POST:
        form = FormNilai(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormNilai()
            berita = Nilai.objects.all()
            data = {
            'berita' : berita,
            'Title' : "Beranda Story.La - Website Literasi",
            'form'  : form,
            }
            return render(request, 'index.html', data)
    else:
        form = FormNilai()
        berita = Nilai.objects.all()
        data = {
           'berita' : berita,
           'Title' : "Beranda Story.La - Website Literasi",
           'form'  : form,
        }
    return render(request, 'index.html', data)


def menuliscerita(request):
    penulis =  Karya.objects.all()
    data = {
        'Title' : "Menulis Cerita - Story.La",
        'penulis' : penulis,
    }
    return render(request, 'menuliscerita.html', data)


def testimonial(request):
    berita =  Nilai.objects.all()
    data = {
        'Title' : "Testimoni - Story.La",
        'berita' : berita,
    }
    return render(request, 'testimonial.html', data)


@login_required(login_url=settings.LOGIN_URL)
def datacerita(request):
    penulis = Karya.objects.all()
    data = {
        'penulis' : penulis,
        'Title' : "Data Cerita",
    }
    return render(request, 'datacerita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def datapenilaian(request):
    berita = Nilai.objects.all()
    data = {
        'berita' : berita,
        'Title' : "Data Penilaian",
    }
    return render(request, 'datapenilaian.html', data)


@login_required(login_url=settings.LOGIN_URL)
def tambahcerita(request):
    if request.POST:
        form = FormKarya(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKarya()
            penulis = Karya.objects.all()
            data = {
            'penulis' : penulis,
            'form'  : form,
            'Title' : "Tambah Cerita - Story.La",
            }
            return render(request, 'tambahcerita.html', data)
    else:
        form = FormKarya()
        penulis = Karya.objects.all()
        data = {
           'penulis' : penulis,
           'form'  : form,
           'Title' : "Tambah Cerita - Story.La",
        }
    return render(request, 'tambahcerita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahnilai(request):
    if request.POST:
        form = FormNilai(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormNilai()
            berita = Nilai.objects.all()
            data = {
            'berita' : berita,
            'form'  : form,
            'Title' : "Tambah Penilaian - Story.La"
            }
            return render(request, 'tambahnilai.html', data)
    else:
        form = FormNilai()
        berita = Nilai.objects.all()
        data = {
           'berita' : berita,
           'form'  : form,
           'Title' : "Tambah Penilaian - Story.La"
        }
    return render(request, 'tambahnilai.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updatecerita(request, id):
    ubahcerita = Karya.objects.get(pk=id)
    if request.POST:
        form = FormKarya(request.POST, instance=ubahcerita)
        if form.is_valid():
            form.save()
            data = {
                'karya' : ubahcerita,
                'form'  : form,
            }
            return render(request, 'updatecerita.html', data)
    else:
        form = FormKarya(instance=ubahcerita)
        data = {
        'karya' : ubahcerita,
        'form'  : form,
        }
    return render(request, 'updatecerita.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updatenilai(request, pl):
    ubahberita = Nilai.objects.get(pk=pl)
    if request.POST:
        if request.FILES:
            ubahberita.gambar.delete()
        form = FormNilai(request.POST, request.FILES, instance=ubahberita)
        if form.is_valid():
            form.save()
            data = {  
                'nilai' : ubahberita,
                'form'  : form,
            }
            return render(request, 'updatenilai.html', data)
    else:
        form = FormNilai(instance=ubahberita)
        data = {
        'nilai' : ubahberita,
        'form'  : form,
        }
    return render(request, 'updatenilai.html', data)


@login_required(login_url=settings.LOGIN_URL) 
def deletecerita(request, id):
    karya = Karya.objects.get(pk=id)
    karya.delete()
    
    return redirect("/datacerita/")


@login_required(login_url=settings.LOGIN_URL) 
def deletenilai(request, pl):
    nilai = Nilai.objects.get(pk=pl)
    nilai.gambar.delete()
    nilai.delete()
    
    return redirect("/datapenilaian/")