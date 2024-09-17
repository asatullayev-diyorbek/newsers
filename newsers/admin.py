from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, News, Email


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'is_banner', 'is_weekly', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description', 'views', 'created_at')
    prepopulated_fields = {'slug': ('title', )}
    # list_filter = ('category', 'is_active', 'created_at')
    list_editable = ('is_active', 'category', 'is_banner', 'is_weekly')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"')
        return mark_safe('<span>Rasm mavjud emas</span>')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email', 'created_at')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Email, EmailAdmin)