from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'category',
        'content',
        'link_text',
    )
    prepopulated_fields = {"slug": ("title",)}
    # list_editable = ('title',)


admin.site.register(Post, PostAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
