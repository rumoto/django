from django.db import models
from django.db.models import UniqueConstraint


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #tags = models.ManyToManyField('Tag', related_name='tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=60, verbose_name='Название')
    articles = models.ManyToManyField(Article, through='Scope', related_name='tags')


    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Тематики статьи')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        constraints = [
            UniqueConstraint(fields=['article', 'tag'], name='unique_host_migration'),
        ]
        ordering = ['-is_main']

