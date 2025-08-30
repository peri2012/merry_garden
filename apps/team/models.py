from django.db import models

class Workers(models.Model):
    fullname = models.CharField(max_length=255,verbose_name="Ф.И.О" )
    discription = models.CharField(max_length=)