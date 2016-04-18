from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields


class Position(TranslatableModel):
    start_date = models.DateField(verbose_name=_('Start date'), help_text=_(
        "The date when you started this position - only the month and year will be displayed"))
    end_date = models.DateField(verbose_name=_('End date'), blank=True, null=True, help_text=_(
        "The date when this position ended - only the month and year will be displayed. You don't have to define this if it is your active post."))
    is_active = models.BooleanField(verbose_name=_("Active position?"), help_text=_(
        "Check this if this is your active post. You won't have to add the end_date in that case."))

    translations = TranslatedFields(
        title=models.CharField(verbose_name=_('Title'), max_length=255),
        company=models.CharField(verbose_name=_('Company'), max_length=255),
        description=models.TextField(verbose_name=_("Description"),
                                     help_text=_("Give a short description about your work and responsibilities."),
                                     max_length=2048,
                                     null=True, blank=True),
        website=models.CharField(verbose_name=_("Website"), help_text=_("Provide a link to the company's website."),
                                 max_length=255),
    )

    def __unicode__(self):
        return self.title


class PositionPlugin(CMSPlugin):
    post = models.ForeignKey(Position)

    def __unicode__(self):
        return self.post.title



