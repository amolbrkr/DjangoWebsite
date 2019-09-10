from django.db import models
from datetime import datetime
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class ArticlePost(models.Model):
  title = models.CharField(max_length=250)
  slug = models.CharField(max_length=100)
  article_content = MarkdownxField(name='article_content')
  date_published = models.DateTimeField(default=datetime.now, blank=True)
  author = models.CharField(max_length=100, default="Masterclass Admin")

  def __str__(self):
    return self.title

  def show_markdown(self):
    return markdownify(self.article_content)
