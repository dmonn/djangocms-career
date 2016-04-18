# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Post


class CareerPlugin(CMSPluginBase):
    module = 'Career'


class CareerContainer(CareerPlugin):
    """
    Container to hold position entries
    """
    name = _("Career Plugin Container")
    render_template = "djangocms_career/career_plugin.html"
    allow_children = True
    child_classes = ['PositionObject']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


class PositionObject(CareerPlugin):
    """
    Position Entries, being held by CareerContainer
    """
    name = _("Position")
    render_template = "djangocms_career/position_object.html"
    require_parent = True
    parent_classes = ['CareerContainer']
    model = Post

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(CareerContainer)
plugin_pool.register_plugin(PositionObject)
