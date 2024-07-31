from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
   
class Lampadaire(models.Model):
        id    = models.AutoField(primary_key=True)
        id_unique=models.CharField(max_length=200)
        id_lampadaire = models.CharField(max_length=200)
        commune = models.CharField(max_length=100)
        zone =models.CharField(blank=True, null=True)
        photo_jour = models.CharField(max_length=200)
        photo_nuit = models.CharField(max_length=200,null=True)
        photo_jour_url = models.URLField(blank=True, null=True)
        photo_nuit_url = models.URLField(blank=True,null=True)
        submitted_by = models.CharField(max_length=200)
        validation = models.CharField(max_length=5,null=True)
        observation = models.CharField(max_length=200 ,null=True)
        date_created = models.DateField(auto_now_add=True)


        def __str__(self):
           return self.id_unique