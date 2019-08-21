# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from struggle_story.models import Article


def index_page(request):
    article_list = Article.objects.all()
    for index, article in enumerate(article_list):
        pass

    return render(request, 'index.html', {"article_list": article_list, "newest_list": article_list})
