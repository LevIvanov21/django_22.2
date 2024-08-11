from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='URL')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
