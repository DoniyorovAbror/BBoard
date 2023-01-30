# Generated by Django 4.1.5 on 2023-01-27 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=64, verbose_name='Название')),
                ('post_content', models.TextField(verbose_name='Контент')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_date', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('SL', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('HS', 'Кузнецы'), ('SK', 'Кожевники'), ('PO', 'Зельевары'), ('SM', 'Мастера заклинаний')], default='TN', max_length=2, unique=True, verbose_name='Название Категории')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('subscribers', models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_content', models.TextField(verbose_name='Текст отклика')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создание')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='Состояния отклика')),
                ('response_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отклика')),
                ('response_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post', verbose_name='Отклик поста')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
