from django.db import models
from datetime import date



class Post(models.Model):

    def number():
        no = Post.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    post_name = models.CharField("Имя треда", max_length = 150)
    post_content = models.TextField("Тело треда",  max_length = 15000)
    post_date = models.DateField("Дата создания", default = date.today)
    url = models.SlugField(max_length=160, unique=True, default=number)

    def __str__(self):
        return self.post_name

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"

