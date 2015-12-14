# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UsefullInformaton.title_ru'
        db.add_column(u'information_usefullinformaton', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UsefullInformaton.body_ru'
        db.add_column(u'information_usefullinformaton', 'body_ru',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.title_ru'
        db.add_column(u'information_news', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.body_ru'
        db.add_column(u'information_news', 'body_ru',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UsefullInformaton.title_ru'
        db.delete_column(u'information_usefullinformaton', 'title_ru')

        # Deleting field 'UsefullInformaton.body_ru'
        db.delete_column(u'information_usefullinformaton', 'body_ru')

        # Deleting field 'News.title_ru'
        db.delete_column(u'information_news', 'title_ru')

        # Deleting field 'News.body_ru'
        db.delete_column(u'information_news', 'body_ru')


    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'information.usefullinformaton': {
            'Meta': {'object_name': 'UsefullInformaton'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['information']