from django.contrib import admin

from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ['author',]
    search_fields = ('title', 'content'),
    list_filter = ('categories',)
    date_hierarchy = 'published'

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías'

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

