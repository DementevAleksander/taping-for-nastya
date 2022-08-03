from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey(
      'Category', on_delete=models.PROTECT,
      related_name='posts',
      verbose_name='Название папки'
    )
    content = models.TextField(verbose_name='Подробный текст', blank=True)
    link_text = models.TextField(verbose_name='Ссылка', default='https://')
    book = models.FileField(upload_to='media/books/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


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
