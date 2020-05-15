from django.db import models
from datetime import date

class Posts(models.Model):
    post_name = models.CharField("Имя треда", max_length = 150)
    post_content = models.TextField("Тело треда",  max_length = 15000)
    post_date = models.DateField("Дата создания", default = date.today)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"

