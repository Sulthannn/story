from django.forms import ModelForm
from django import forms
from .models import *

class FormKarya(ModelForm):
    class Meta:
        model = Karya
        fields = '__all__'

        widgets = {
            'penulis' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Penulis', 'required':'required'}),
            'email' : forms.TextInput({'type':'email','class':'form-control', 'placeholder':'Email', 'required':'required'}),
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'kota' : forms.TextInput({'class':'form-control', 'placeholder':'Kota Penulis', 'required':'required'}),
            'judul' : forms.TextInput({'class':'form-control', 'placeholder':'Judul', 'required':'required'}),
            'karangan' : forms.Textarea({'class':'form-control', 'placeholder':'Cerita Anda', 'required':'required'}),    
            'kreasi_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Kreasi', 'required':'required'}),
        }


class FormNilai(ModelForm):
    class Meta:
        model = Nilai
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Anda', 'required':'required'}),
            'email' : forms.TextInput({'type':'email','class':'form-control', 'placeholder':'Email Anda', 'required':'required'}),
            'gambar' : forms.FileInput({'class':'form-control', 'placeholder':'Gambar', 'required':'required'}),
            'komentar' : forms.Textarea({'class':'form-control', 'placeholder':'Komentar', 'required':'required'}),
            'status_id' : forms.Select({'class':'form-control', 'placeholder':'Status Penilaian', 'required':'required'}),
        }
        
