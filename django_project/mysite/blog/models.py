from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# 增加自定义的管理器
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # 自定义管理器,很重要的设定
    objects = models.Manager()        #默认的管理器
    published = PublishedManager()     #自定义管理器

    # 构建URL,reverse反向解析url
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title




