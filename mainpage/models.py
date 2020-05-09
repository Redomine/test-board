from django.db import models

class Posts(models.Model):
    name = models.CharField("Имя треда", max_length = 150)
    description = models.TextField("Тело треда",  max_length = 15000)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"