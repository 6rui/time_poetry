# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# 文章 数据模型对象
class Article(models.Model):
    # 文章的id
    id = models.AutoField(primary_key=True)
    # 文章的主标题
    title = models.TextField(max_length=256, null=False, default='new article')
    # 文章的副标题
    sub_title = models.TextField(max_length=256, null=True, default='sub title')
    # 文章标签类型
    tag_type = models.SmallIntegerField(null=False, default=0, db_index=True)
    # 文章摘要
    summary = models.TextField(max_length=256, null=True, default='summary')
    # 文章内容
    content = models.TextField(null=False, default='this is an article!')
    # 文章作者id
    author_id = models.IntegerField(null=False, default=0, db_index=True)
    # 文章创建时间
    create_time = models.DateTimeField(null=False, auto_now_add=True)
    # 文章发布时间
    publish_time = models.DateTimeField(null=False, auto_now_add=True)
    # 文章最后修改时间
    last_update_time = models.DateTimeField(null=False, auto_now=True),
    # 文章发布状态
    publish_state = models.SmallIntegerField(null=False, default=0)
    # 文章所属分类id
    category_id = models.IntegerField(null=False, default=0, db_index=True)

    def __str__(self):
        return self.title
