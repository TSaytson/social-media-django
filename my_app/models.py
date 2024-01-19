from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=10, verbose_name='Categoria')
  description = models.TextField(null=True, blank=True)

  def __str__(self) -> str:
    return self.name
  
  class Meta:
    verbose_name = 'Categoria'

class Post(models.Model):
  title = models.CharField(max_length=15, verbose_name='Título')
  subtitle = models.CharField(max_length=30, null=True, blank=True, verbose_name='Subtítulo')
  content = models.TextField(verbose_name='Conteúdo')
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Autor')
  categories = models.ManyToManyField(Category)

  def __str__(self) -> str:
    return self.title
  
  class Meta:
    verbose_name = 'Artigo'
    # verbose_name_plural = 'Artigos'