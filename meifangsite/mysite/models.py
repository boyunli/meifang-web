# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.utils import timezone
from django.db import models

class BaseModel(models.Model):
    create_time = models.DateTimeField(default=timezone.now,
            verbose_name='创建时间', editable=False)
    update_time = models.DateTimeField(default=timezone.now,
            verbose_name='更新时间', editable=False)

    def save(self, update_time=None, *args, **kwargs):
        self.update_time = update_time or timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

    def __str__(self):
        return unicode(self)

    class Meta:
        abstract = True


class GovWeb(BaseModel):
    LEVEL_DEFAULT = 999

    title = models.CharField(max_length=200, verbose_name='网页标题', null=True, blank=True)
    network_platform = models.CharField(max_length=100, verbose_name='网络平台')
    url = models.CharField(max_length=200, verbose_name='文章链接')
    has_crawl = models.BooleanField(default=False, verbose_name='是否抓取')
    has_parser = models.BooleanField(default=False, verbose_name='是否解析')
    level = models.IntegerField(default=LEVEL_DEFAULT)

    def __unicode__(self):
        return u'network_platform={network_platform},'\
                .format(network_platform=self.network_platform)

    #def save(self, *args, **kwargs):
    #    if not self.author:
    #        self.author = self.network_platform
    #    super(GovWeb, self).save(*args, **kwargs)

    class Meta:
        db_table = 'gov_web'
        verbose_name = verbose_name_plural = '政府网站'

class EstateWeb(BaseModel):

    network_platform = models.CharField(max_length=100, verbose_name='网络平台')
    url = models.CharField(max_length=200, verbose_name='文章链接')

    def __unicode__(self):
        return u'network_platform={network_platform},'\
                .format(network_platform=self.network_platform)

    class Meta:
        db_table = 'estate_web'
        verbose_name = verbose_name_plural = '房产网站'

class SNSWeb(BaseModel):

    author = models.CharField(max_length=200, verbose_name='作者', null=True, blank=True)
    network_platform = models.CharField(max_length=100, verbose_name='网络平台')
    url = models.CharField(max_length=200, verbose_name='文章链接')

    def __unicode__(self):
        return u'author={author}, network_platform={network_platform},'\
                .format(author=self.author, network_platform=self.network_platform)

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = self.network_platform
        super(SNSWeb, self).save(*args, **kwargs)

    class Meta:
        db_table = 'sns_web'
        verbose_name = verbose_name_plural = 'SNS平台'

class WeiXin(BaseModel):

    author = models.CharField(max_length=200, verbose_name='作者', null=True, blank=True)
    network_platform = models.CharField(max_length=100, verbose_name='网络平台')
    url = models.CharField(max_length=200, verbose_name='文章链接')

    def __unicode__(self):
        return u'author={author}, network_platform={network_platform},'\
                .format(author=self.author, network_platform=self.network_platform)

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = self.network_platform
        super(WeiXin, self).save(*args, **kwargs)

    class Meta:
        db_table = 'weixin'
        verbose_name = verbose_name_plural = '微信'
