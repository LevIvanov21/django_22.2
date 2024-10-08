# Generated by Django 4.2 on 2024-08-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='URL')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
