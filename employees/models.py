# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

class Employee(MPTTModel):
    parent = models.ForeignKey('Employee', null=True)
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("First name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last name"))
    second_name = models.CharField(max_length=255, verbose_name=_("Second name"))
    post = models.CharField(max_length=255, verbose_name=_("Post"))

    def __unicode__(self):
        return u'%s - %s %s %s' % (self.first_name, self.second_name, self.last_name, self.post)

    class Meta:
        verbose_name = _(u"Employee")
        verbose_name_plural = _(u"Employees")



class TelephoneNumber(models.Model):
    employee = models.ForeignKey(Employee)
    number = models.CharField(max_length=255, verbose_name=_("Number"))

    def __unicode__(self):
        return u'%s' % (self.number)

    class Meta:
        verbose_name = _(u"TelephoneNumber")
        verbose_name_plural = _(u"TelephoneNumbers")


class Email(models.Model):
    employee = models.ForeignKey(Employee)
    email = models.CharField(max_length=255, verbose_name=_("Email"))

    def __unicode__(self):
        return u'%s' % (self.email)

    class Meta:
        verbose_name = _(u"Email")
        verbose_name_plural = _(u"Emails")

class SkypeName(models.Model):
    employee = models.ForeignKey(Employee)
    skype_name = models.CharField(verbose_name=_("Skype"), max_length=255)

    def __unicode__(self):
        return u'%s' % (self.skype_name)

    class Meta:
        verbose_name = _(u"Skype")
        verbose_name_plural = _(u"Skype records")
