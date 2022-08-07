from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'serial_number',
        'category',
        'title',
        # 'slug',
        'content',
        'link_text',
        'book'
    )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category',)
    list_editable = ('serial_number',)


admin.site.register(Post, PostAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
