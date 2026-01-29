from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "author"]
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
