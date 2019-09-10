from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import ArticlePost

admin.site.register(ArticlePost, MarkdownxModelAdmin)
