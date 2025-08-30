from django.db import models

# Create your models here.


class ToBook(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    date = models.CharField(max_length=255, verbose_name="Дата")
    adults_quantity = models.IntegerField(verbose_name="Взрослые")
    childs_quantity = models.IntegerField(verbose_name="Дети")

    def __str__(self):
        return f"{self.fullname} || {self.phone} || {self.date}"
    
    class Meta:
        verbose_name = "Заброн"
        verbose_name_plural = "Заброны"