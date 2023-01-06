from django.db import models

# Create your models here.

class Kreasi(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Karya(models.Model):
   penulis = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   koordinat = models.CharField(max_length=100)
   kota = models.CharField(max_length=100)
   judul = models.CharField(max_length=100)
   karangan = models.TextField()
   kreasi_id = models.ForeignKey(Kreasi, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.penulis



class Status(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Nilai(models.Model):
   nama = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   gambar = models.FileField(upload_to='testi/', null=True)
   komentar = models.CharField(max_length=100)
   status_id = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.nama
