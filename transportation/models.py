# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel
from django.core.exceptions import ValidationError
from math import fabs

class LongitudeValidator(object):
    message = _('Enter longitude value from diapason [-90, 90]')
    code = 'invalid_longitude'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        if fabs(value) > 90:
            raise ValidationError(self.message, code=self.code)


class LatitudeValidator(object):
    message = _('Enter latitude value from diapason [-180, 180]')
    code = 'invalid_latitude'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        if fabs(value) > 180:
            raise ValidationError(self.message, code=self.code)


class TransportationsGeography(MPTTModel):
    parent = models.ForeignKey('TransportationsGeography', null=True)
    title = models.CharField(verbose_name=_(u"Title"), max_length=255, blank=True)
    description = models.CharField(verbose_name=_(u"Description"), max_length=255, blank=True)
    longitude = models.FloatField(verbose_name=_(u"Longitude"), validators=[LongitudeValidator])
    latitude = models.FloatField(verbose_name=_(u"Latitude"), validators=[LatitudeValidator], default=53.9000000)

    class Meta:
        verbose_name = _(u"Transportation Point")
        verbose_name_plural = _(u"Points of transportation")
        db_table="transporation_transportationsgeography"
