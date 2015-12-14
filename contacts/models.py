# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

class Contact(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")

class OfficeContact(Contact):
    address = models.CharField(max_length=255, verbose_name=_("Address"))

    def __unicode__(self):
        return u'%s' % (self.address)

    class Meta:
        verbose_name = _(u"Office Contact")
        verbose_name_plural = _(u"Office Contacts")



class Employee(Contact):
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
    contact = models.ForeignKey(Contact)
    number = models.CharField(max_length=255, verbose_name=_("Number"))

    def __unicode__(self):
        return u'%s' % (self.number)

    class Meta:
        verbose_name = _(u"TelephoneNumber")
        verbose_name_plural = _(u"TelephoneNumbers")


class Email(models.Model):
    contact = models.ForeignKey(Contact)
    email = models.CharField(max_length=255, verbose_name=_("Email"))

    def __unicode__(self):
        return u'%s' % (self.email)

    class Meta:
        verbose_name = _(u"Email")
        verbose_name_plural = _(u"Emails")

class SkypeName(models.Model):
    contact = models.ForeignKey(Contact)
    skype_name = models.CharField(verbose_name=_("Skype"), max_length=255)

    def __unicode__(self):
        return u'%s' % (self.skype_name)

    class Meta:
        verbose_name = _(u"Skype")
        verbose_name_plural = _(u"Skype records")



class FaxNumber(models.Model):
    contact = models.ForeignKey(Contact)
    fax_number = models.CharField(verbose_name=_("Fax"), max_length=255)

    def __unicode__(self):
        return u'%s' % (self.fax_number)

    class Meta:
        verbose_name = _(u"Fax")
        verbose_name_plural = _(u"Fax numbers")


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u"Your name"))
    number = models.CharField(max_length=255, verbose_name=_(u"Contact number"), null=True, blank=True)
    email = models.EmailField(verbose_name=_(u"Email"))
    message = models.TextField(verbose_name=_(u"Your message"))


    class Meta:
        verbose_name = _(u"User message")
        verbose_name_plural = _(u"User messages")