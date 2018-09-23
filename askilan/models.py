from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    ad = models.CharField(max_length=20)
    soyad = models.CharField(max_length=20)
    email = models.EmailField()
    ilan = models.ForeignKey('Ilan', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ad + " " +  self.soyad

    def __unicode__(self):
        return self.ad + " " +  self.soyad


class Ilan(models.Model):
    baslik = models.CharField(max_length=40)
    metin = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    gosterim_sayisi = models.IntegerField(default=0)

    def __str__(self):
        return self.baslik + " - " + str(self.olusturma_tarihi)

    def __unicode__(self):
        return self.baslik
