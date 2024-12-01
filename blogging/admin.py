from django.contrib import admin
from .models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'modified_date', 'published_date')
    search_fields = ('title', 'author__username')
    list_filter = ('published_date', 'author')
    date_hierarchy = 'created_date'
    inlines = [CategoryInline]
    ordering = ('-created_date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
