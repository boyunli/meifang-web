# -*- coding:utf-8 -*-

import logging

from django.contrib.auth.models import Group, User

import xadmin
from xadmin import views

from .models import  InputContent

logger = logging.getLogger('mysite')


class MainDashboard(object):
    title = '管理系统首页'

xadmin.sites.site.register(views.website.IndexView, MainDashboard)


class GlobalSetting(object):
    site_title = u'美房网内容管理系统'
    site_footer = u'美房网内容管理系统'
    menu_style = 'default'
    global_search_models = [ InputContent,]

    apps_icons = {
            'mysite': 'fa fa-cloud',
            }
    global_models_icon = {
            InputContent: 'fa fa-list-alt',
            }

xadmin.sites.site.register(views.CommAdminView, GlobalSetting)


class InputContentAdmin(object):
    list_display = ('id', 'author', 'network_platform', 'url')
    list_display_links = ('url',)
    search_fields = ['author', 'network_platform']

xadmin.sites.site.register(InputContent, InputContentAdmin)

xadmin.sites.site.unregister(Group)
xadmin.sites.site.unregister(User)
