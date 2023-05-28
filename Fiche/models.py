from django.db import models

# Create your models here.


class Fiches(models.Model):
    CLASSES=(('Sixième','Sixième'),
             ('Cinquième','Cinquième'),
             ('Quatrième','Quatrième'),
             ('Troisième','Troisième'))
    THEME=(('Calcul numerique','Calcul numérique'),
             ('Application du plan','Application du plan'),
             ('Configuration du plan','Configuration du plan'),
             ('Organisation de données','Organisation de données'))
    lecon=models.CharField(max_length=200,null=True)
    theme=models.CharField(max_length=200,null=True,choices=THEME)
    niveau=models.CharField(max_length=200,null=True,choices=CLASSES)
    fiche=models.FileField(upload_to='fiches/')    
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.lecon