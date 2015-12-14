# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Partner(models.Model):
    company_name = models.CharField(max_length=255, verbose_name=_("Company name"))
    logotype = models.ImageField(upload_to='images/service', verbose_name=_("Logo"))
    url = models.URLField(verbose_name=_('URL'))

    def __unicode__(self):
        return self.company_name

    class Meta:
        verbose_name = _(u"Partner")
        verbose_name_plural = _(u"Partners")