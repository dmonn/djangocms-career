from datetime import datetime
from dateutil import relativedelta
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField


class Post(CMSPlugin):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    company = models.CharField(verbose_name=_('Company'), max_length=255)
    start_date = models.DateField(verbose_name=_('Start date'), help_text=_(
        "The date when you started this position - only the month and year will be displayed"))
    end_date = models.DateField(verbose_name=_('End date'), blank=True, null=True, help_text=_(
        "The date when this position ended - only the month and year will be displayed. You don't have to define this if it is your active post."))

    active_post = models.BooleanField(verbose_name=_("Active position?"), help_text=_(
        "Check this if this is your active post. You won't have to add the end date in that case."))

    description = HTMLField(verbose_name=_("Description"),
                                   help_text=_("Give a short description about your work and responsibilities."),
                                   max_length=2048,
                                   null=True, blank=True)

    website = models.CharField(verbose_name=_("Website"), help_text=_("Provide a link to the company's website."),
                               max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_month_diff(self, d1, d2):
        """
        Counting up the months from d1 (start date)
        Until d2 (end date OR today) is reached.

        Args:
            d1: Start Date
            d2: End date

        Returns: Months

        """

        delta = relativedelta.relativedelta(d2, d1)
        months = (delta.years*12) + delta.months

        return months

    @property
    def get_month_diff_string(self):
        """
        Simple method to humanize the months from function
        get_month_diff

        Returns: diff_string
        """

        if self.active_post:
            d2 = datetime.now()
        else:
            d2 = self.end_date

        month_diff = int(self.get_month_diff(self.start_date, d2))
        if month_diff < 12:
            diff_string = (str(month_diff) + ' ' + str(_('Months')))
            if month_diff <= 1:
                diff_string = (str(1) + ' ' + str(_('Month')))
        else:
            if month_diff % 12 == 0:
                year_diff = str(month_diff/12)
            else:
                year_diff = str(round(float(month_diff)/12, 1))
                print(year_diff)
            diff_string = (year_diff + ' ' + str(_('Years')))
            if year_diff == '1':
                diff_string = (str(1) + ' ' + str(_('Year')))

        return diff_string

    @property
    def get_relative_length(self):
        """
        Method to get the relative length to
        the longest length.
        Everything below 18% gets up'd to 18% (design reasons)

        Returns: length_percentage
        """

        longest_post = self.get_longest_post()

        if self.active_post:
            end_date = datetime.now()
        else:
            end_date = self.end_date

        relative_percentage = (float(self.get_month_diff(self.start_date, end_date)) / float(longest_post)) * 100

        if relative_percentage <= 18:
            length_percentage = 18
        else:
            length_percentage = relative_percentage

        return int(length_percentage)

    def get_longest_post(self):
        """
        Get the post object with the longest duration

        Returns: longest (amount of months)

        """
        longest = 0
        for post in Post.objects.all():

            if post.active_post:
                d2 = datetime.now()
            else:
                d2 = post.end_date

            diff = self.get_month_diff(post.start_date, d2)

            if diff > longest:
                longest = diff

        return longest
