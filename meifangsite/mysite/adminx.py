# -*- coding:utf-8 -*-

import logging

from django.contrib.auth.models import Group, User

import xadmin
from xadmin import views

from .models import  GovWeb,\
        EstateWeb,\
        SNSWeb,\
        WeiXin


logger = logging.getLogger('mysite')


class MainDashboard(object):
    title = '管理系统首页'

xadmin.sites.site.register(views.website.IndexView, MainDashboard)


class GlobalSetting(object):
    site_title = u'美房网舆情监控系统'
    site_footer = u'美房网舆情监控系统'
    menu_style = 'default'
    global_search_models = [ GovWeb,]

    apps_icons = {
            'mysite': 'fa fa-cloud',
            }
    global_models_icon = {
            GovWeb: 'fa fa-list-alt',
            }

xadmin.sites.site.register(views.CommAdminView, GlobalSetting)


class GovWebAdmin(object):
    list_display = ('id', 'network_platform', 'url')
    list_display_links = ('network_platform', )
    #list_editable = ('has_crawl',)
    search_fields = ['network_platform']
    list_export = ()

xadmin.sites.site.register(GovWeb, GovWebAdmin)

class EstateWebAdmin(object):
    list_display = ('id', 'network_platform', 'url')
    list_display_links = ('network_platform', )
    #list_editable = ('has_crawl',)
    search_fields = ['network_platform']
    list_export = ()

xadmin.sites.site.register(EstateWeb, EstateWebAdmin)

class SNSWebAdmin(object):
    list_display = ('id', 'network_platform', 'url')
    list_display_links = ('network_platform', )
    #list_editable = ('has_crawl',)
    search_fields = ['network_platform']
    list_export = ()

xadmin.sites.site.register(SNSWeb, SNSWebAdmin)

class WeiXinAdmin(object):
    list_display = ('id', 'network_platform', 'url')
    list_display_links = ('network_platform', )
    #list_editable = ('has_crawl',)
    search_fields = ['network_platform']
    list_export = ()

xadmin.sites.site.register(WeiXin, WeiXinAdmin)

xadmin.sites.site.unregister(Group)
xadmin.sites.site.unregister(User)
