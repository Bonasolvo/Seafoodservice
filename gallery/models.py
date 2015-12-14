# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

from fields import ExtFileField


class PhotoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    photo = ExtFileField(upload_to='photos', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    title = models.CharField(max_length=255, blank=True, verbose_name=_("Title"))
    add_this_photo_to_slide = models.BooleanField(null=False, verbose_name=_(u"Add this photo to slide"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))

    def __unicode__(self):
        return self.photo.name

    class Meta:
        verbose_name = _(u"Photo")
        verbose_name_plural = _(u"Photos")


import random


def get_path_and_name(instance, filename):
    letters = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ext = filename.lower().split('.')[-1]
    instance.filename =  u'videos/'+u''.join(random.choice(letters) for x in xrange(31))+u'_c.'+ext

    return instance.filename


class VideoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    video_image = ExtFileField(upload_to='videos/images', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"),
                             default="css/images/slide3.png")
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))

    def __unicode__(self):
        return ("%s - %s")%(self.video_image, self.description)

    def to_dict(self):
        return {
            'video_image':self.video_image,
            'description':self.description,
        }

    class Meta:
        verbose_name = _(u"Video")
        verbose_name_plural = _(u"Videos")


video_ext = (".mp4", ".ogg", ".webm", '.avc', '.3gp', '.avi','.flv')

class VideoFile(models.Model):
    video = models.ForeignKey(VideoGallery, null=False)
    file = ExtFileField(upload_to=get_path_and_name, verbose_name=_("video"),
                         ext_whitelist=video_ext,
                         help_text=u"Большинство браузеров поддерживают файлы с расширением .mp4, .ogg или .webm. "+
                                   u"Файл для загрузки должен иметь разрешение %s"%(" ".join(i for i in video_ext)))
    type = models.CharField(verbose_name=_("Extension of video"), max_length=15, default='video/mp4')

    def __unicode__(self):
        return ("%s - %s")%(self.file, self.type)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.type = u'video/' + self.file.name.lower().split('.')[-1]
        return super(VideoFile, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = _(u"Video")
        verbose_name_plural = _(u"Videos")