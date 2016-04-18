# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class CareerApp(CMSApp):
    name = _("Career App")
    urls = ["djangocms_career.urls", ]

apphook_pool.register(CareerApp)

