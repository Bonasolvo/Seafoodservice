# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel


class Certificate(MPTTModel):
    parent = models.ForeignKey('Certificate', null=True)
    image = models.ImageField(upload_to="images/certificates", verbose_name=_("Certificate image"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    def __unicode__(self):
        return u'%s - %s' % (self.image, self.description)

    class Meta:
        verbose_name = _(u"Certificate")
        verbose_name_plural = _(u"Certificates")

