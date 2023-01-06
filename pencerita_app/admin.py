from django.contrib import admin

# Register your models here.
from .models import *

class olahkarya(admin.ModelAdmin):
    list_display = ['penulis', 'email', 'koordinat', 'judul', 'karangan']
    search_fields = ['penulis', 'judul']
    list_filter = ['kreasi_id']
    list_per_page = 5

admin.site.register(Karya, olahkarya)
admin.site.register(Kreasi)

class olahnilai(admin.ModelAdmin):
    list_display = ['nama', 'email', 'gambar', 'komentar']
    search_fields = ['nama', 'komentar']
    list_filter = ['status_id']
    list_per_page = 5

admin.site.register(Nilai, olahnilai)
admin.site.register(Status)