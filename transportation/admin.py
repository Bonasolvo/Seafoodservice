# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
from mptt.forms import forms
from models import TransportationsGeography

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)
        self.fields['longitude'].initial = 27.5666700
        self.fields['latitude'].initial = 53.9000000



class TransportationsGeographyAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['id', 'title', 'description', 'longitude', 'latitude']
    form = MPTTAdminForm
    change_form_template = 'admin/transporation/transportationsgeography/change_form.html'
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
                'title',
                'description',
                'longitude',
                'latitude'
            ]
        }),
    ]

admin.site.register(TransportationsGeography, TransportationsGeographyAdmin)