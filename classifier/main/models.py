from django.db import models
from django.contrib.auth.models import UserManager


class TagsModel(models.Model):
    tagName = models.TextField(db_column='tagName', unique=True)
    tagId = models.AutoField(db_column='tagId', primary_key=True)

    class Meta:
        managed = True
        db_table = 'texts_tags'

    def __str__(self):
        return str(self.tagId)


class Story(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=150)
    classif = models.CharField('Категория', max_length=150)
    story = models.TextField('Краткое содержание')

    objects = UserManager()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Сказка'
        verbose_name_plural = 'Сказки'

class Resume(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name

class New(models.Model):  # наши новости
    tag_news = models.TextField(db_column='Tag', unique=True)
    title_news = models.TextField(db_column='Title_news', unique=True)
    text_news = models.TextField(db_column='Text_news', unique=True)

    def __str__(self):
        return self.title_news

    class Meta:
        managed = True
        db_table = 'texts'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'