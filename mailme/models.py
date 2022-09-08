from django.db import models



class Mailme(models.Model): 
    nom   = models.CharField(max_length=128, verbose_name="Nom Complet")
    tel   = models.CharField(max_length=128, verbose_name="Téléphone")
    email = models.CharField(max_length=128, verbose_name="E-mail")

    def __str__(self) :
        return self.nom
