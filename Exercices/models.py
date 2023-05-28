from django.db import models

# Create your models here.

class Exercice(models.Model):
    CLASSES=(('Sixième','Sixième'),
             ('Cinquième','Cinquième'),
             ('Quatrième','Quatrième'),
             ('Troisième','Troisième'))
    nom=models.CharField(max_length=200,null=True)
    niveau=models.CharField(max_length=200,null=True,choices=CLASSES)
    fichier=models.FileField(upload_to='fichier/')    
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    correction=models.FileField(upload_to='fichier/')
    def get_absolute_url(self):
        return "/media/%s" %self.fichier
    def __str__(self):
        return self.nom