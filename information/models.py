# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField

class News(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name="related")
    title_image = models.ImageField(upload_to="image/news_title", null=True)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    body = HTMLField(verbose_name=_("Body"))
    date = models.DateField(verbose_name=_("Date"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"News Item")
        verbose_name_plural = _(u"News")


class UsefullInformation(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name="related")
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    body = HTMLField(verbose_name=_("Body"))
    date = models.DateField(verbose_name=_("Date"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Useful information item")
        verbose_name_plural = _(u"Useful information")


class MainPage(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name="related")
    body = HTMLField(verbose_name=_("Body"))

    def __unicode__(self):
        return self.body

    class Meta:
        verbose_name = _(u"Main Page")
        verbose_name_plural = _(u"Main Page")
