from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Başlık",max_length=150)
    completed = models.BooleanField(verbose_name="tamamlandı mı ")

    def __str__(self):
        return self.title,self.completed