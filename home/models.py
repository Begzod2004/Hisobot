from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import *
from datetime import *
# Create your models here.

class Hisobot(models.Model):
    project = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return f"{self.project}"


class Daromad(models.Model):
    daromad = models.IntegerField()
    mijozlar_soni = models.IntegerField()
    time = models.DateTimeField(default=datetime.now, blank=True)
    hisobot = models.ForeignKey(Hisobot, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.daromad}"


class Xarajatlar(models.Model):
    count = models.IntegerField()
    reklama = models.IntegerField()
    time = models.DateTimeField(default=datetime.now, blank=True)
    hisobot = models.ForeignKey(Hisobot, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.count}"





class Drektor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"



class Category(models.Model):
    title = models.CharField(max_length=50)
    drektor = models.ForeignKey(Drektor, on_delete=models.CASCADE)
    daromad = models.ForeignKey(Daromad, on_delete=models.CASCADE)
    xarajatlar = models.ForeignKey(Xarajatlar, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.title}"