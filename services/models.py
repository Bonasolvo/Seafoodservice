# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

class Service(MPTTModel):
    parent = models.ForeignKey('Service', null=True)
    image = models.ImageField(upload_to='images/service')
    description = models.CharField(max_length=255, verbose_name=_("Description"))
    is_fundamental_service = models.BooleanField(verbose_name=_("Is fundamental service?"))

    def __unicode__(self):
        return u'%s %s' % (self.description, "( %s )"%self.description if self.description else "")

    class Meta:
        verbose_name = _(u"Service")
        verbose_name_plural = _(u"Services")
