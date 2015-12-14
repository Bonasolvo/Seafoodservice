# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.forms import forms
from modeltranslation.admin import TranslationAdmin

from models import Certificate
from seafoodservice import settings

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)

class CertificateAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['certificate', 'title_ru', 'title_en', 'description_ru', 'description_en']
    search_fields = ['title_ru', 'title_en', 'description_ru', 'description_en' ]
    form = MPTTAdminForm

    def certificate(self, obj):
        return '<span style="width:20px;height:20px;"><img style="width:80px;height:80px;" src="%s" /></span>'%(settings.MEDIA_URL+obj.image.name)
    certificate.allow_tags = True

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
                'image',
                'title',
                'description',
            ]
        }),
    ]


admin.site.register(Certificate, CertificateAdmin)