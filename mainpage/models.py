from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import utc
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    def number():
        no = Post.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    post_name = models.CharField("Имя треда", max_length = 150)
    post_content = models.TextField("Тело треда",  max_length = 15000)
    post_date = models.DateTimeField("Дата создания", default = datetime.datetime.utcnow().replace(tzinfo=utc))

    def __str__(self):
        return self.post_name

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"


class Comment(models.Model):

    parent_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_content = models.TextField("Тело комментария",  max_length = 15000)
    comment_date = models.DateField("Дата создания", default = datetime.datetime.utcnow().replace(tzinfo=utc))

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"