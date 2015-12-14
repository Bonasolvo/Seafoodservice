# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
from mptt.forms import forms
import os

from models import PhotoGallery, VideoGallery, VideoFile
from seafoodservice import settings

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)

def add_to_gallery(modeladmin, request, queryset):
    queryset.update(add_this_photo_to_gallery=True)
add_to_gallery.short_description = u"Добавить выбранные фотографии в галерею"


def add_to_slider(modeladmin, request, queryset):
    queryset.update(add_this_photo_to_slide=True)
add_to_slider.short_description = u"Добавить выбранные фотографии в слайдер"


class PhotoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['image', 'title', 'description']
    search_fields = ['description_ru', 'description_en']
    list_filter = ['add_this_photo_to_slide', 'add_this_photo_to_gallery']
    form = MPTTAdminForm

    actions = [add_to_gallery, add_to_slider]

    def image(self, obj):
        return '<span style="width:20px;height:20px;"><img style="width:80px;height:80px;" src="%s" /></span>' % (settings.MEDIA_URL+obj.photo.name)
    image.allow_tags = True

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (None, {
            'fields': [
                'photo',
                'title',
                'description',
                'add_this_photo_to_slide',
                'add_this_photo_to_gallery',
            ]
        }),
    ]

class VideoFileAdmin(admin.StackedInline):
    model = VideoFile
    extra = 1

    fieldsets = (None, {
            'fields': [
                'file',
            ]
        }),



class VideoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['image', 'description']
    search_fields = ['description_ru', 'description_en' ]
    inlines = [VideoFileAdmin, ]
    form = MPTTAdminForm

    def image(self, obj):
        return '<span><img style="max-width:100px;height:60px;" src="%s" /></span>'%(settings.MEDIA_URL+obj.video_image.name)
    image.allow_tags = True

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (None, {
            'fields': [
                'video_image',
                'description',
            ]
        }),
    ]


admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)