from django.db import models
from django.urls import reverse


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Садържание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата на публикация')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Снимка', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Побликувано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование на категориите')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
