from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    serial_number = models.TextField(
        max_length=5,
        blank=True,
        verbose_name='№п/п',
    )
    category = TreeForeignKey(
      'Category', on_delete=models.PROTECT,
      related_name='posts',
      verbose_name='Название папки'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название видео'
    )
    content = models.TextField(verbose_name='Текст над видео', blank=True)
    link_text = models.TextField(verbose_name='Ссылка на ютуб', blank=True)
    book = models.FileField(
        verbose_name='PDF-файл',
        upload_to='books/',
        blank=True
    )
    name_book = models.TextField(
        verbose_name='Текст PDF-кнопки',
        blank=True,
        max_length=150
    )
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['serial_number']


class Category(MPTTModel):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Папка'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='Родительская папка'
    )
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Папку'
        verbose_name_plural = 'Папки'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
