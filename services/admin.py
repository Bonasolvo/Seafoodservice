# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
from mptt.forms import forms
from models import Service

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)

class ServiceAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['image', 'description', 'is_fundamental_service']
    list_filter = ['is_fundamental_service']
    form = MPTTAdminForm

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
                'description',
                'is_fundamental_service'
            ]
        }),
    ]

admin.site.register(Service, ServiceAdmin)