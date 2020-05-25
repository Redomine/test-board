from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import utc
from django.contrib.postgres.fields import ArrayField


class Tred(models.Model):
    def number():
        no = Tred.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    tred_name = models.CharField("Имя треда", max_length = 150)
    tred_content = models.TextField("Тело треда",  max_length = 15000)
    tred_date = models.DateTimeField("Дата создания", default = datetime.datetime.utcnow().replace(tzinfo=utc))

    def __str__(self):
        return self.tred_name

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"


class Comment(models.Model):

    tred_parent = models.ForeignKey(Tred, verbose_name="Родительский тред", on_delete=models.CASCADE)
    comment_parent = models.ForeignKey(
        'self', verbose_name="Родительский комментарий", on_delete=models.SET_NULL, blank=True, null=True
    )
    comment_content = models.TextField("Тело комментария",  max_length = 15000)
    comment_date = models.DateField("Дата создания", default = datetime.datetime.utcnow().replace(tzinfo=utc))

    def __str__(self):
        return self.comment_content[0:200]

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"