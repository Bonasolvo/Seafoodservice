# coding: utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config
from django.db import models


from models import News, UsefullInformation, MainPage
from seafoodservice import settings
import datetime

__widget__ = SummernoteWidget if summernote_config['iframe'] \
    else SummernoteInplaceWidget

class NewsAdmin(SummernoteModelAdmin):
    search_fields = ['title_ru', 'title_en', 'body_ru', 'body_en' ]
    list_display = ('id', 'image', 'title', 'body_as_html', 'date')

    formfield_overrides = {
        models.ImageField: {'required': False},
        models.TextField: {'widget': __widget__}
    }

    def body_as_html(self, obj):
        return obj.body
    body_as_html.allow_tags = True

    def image(self, obj):
        if(obj.title_image):
            return '<span style="width:20px;height:20px;"><img style="width:80px;height:80px;" src="%s" /></span>' % (settings.MEDIA_URL+obj.title_image.name)
        return ''
    image.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.date = datetime.datetime.now().date()
        return super(NewsAdmin, self).save_model(request, obj, form, change)

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
                'title_image',
                'title_ru',
                'body_ru',
                'title_en',
                'body_en',
            ]
        }),
    ]


class InformationAdmin(SummernoteModelAdmin):
    search_fields = ['title_ru', 'title_en', 'body_ru', 'body_en' ]
    list_display = ('title', 'body_as_html')

    def body_as_html(self, obj):
        return obj.body
    body_as_html.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.date = datetime.datetime.now().date()
        return super(InformationAdmin, self).save_model(request, obj, form, change)

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
                'title_ru',
                'body_ru',
                'title_en',
                'body_en',
                ]
        }),
    ]


class MainPageAdmin(SummernoteModelAdmin):
    search_fields = ['body_ru', 'body_en' ]
    list_display = ['id', 'body_as_html_ru', 'body_as_html_en']

    def body_as_html_ru(self, obj):
        return obj.body_ru
    body_as_html_ru.allow_tags = True

    def body_as_html_en(self, obj):
        return obj.body_en
    body_as_html_en.allow_tags = True

    def has_add_permission(self, request):
        if(MainPage.objects.all().count()<1):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return None


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
                'body_ru',
                'body_en',
            ]
        }),
    ]


admin.site.register(MainPage, MainPageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(UsefullInformation, InformationAdmin)