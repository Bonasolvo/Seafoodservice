# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UsefullInformaton.title_en'
        db.alter_column(u'information_usefullinformaton', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'UsefullInformaton.body_en'
        db.alter_column(u'information_usefullinformaton', 'body_en', self.gf('tinymce.models.HTMLField')(null=True))

        # Changing field 'News.title_en'
        db.alter_column(u'information_news', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'News.body_en'
        db.alter_column(u'information_news', 'body_en', self.gf('tinymce.models.HTMLField')(null=True))

    def backwards(self, orm):

        # Changing field 'UsefullInformaton.title_en'
        db.alter_column(u'information_usefullinformaton', 'title_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'UsefullInformaton.body_en'
        db.alter_column(u'information_usefullinformaton', 'body_en', self.gf('tinymce.models.HTMLField')(default=None))

        # Changing field 'News.title_en'
        db.alter_column(u'information_news', 'title_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'News.body_en'
        db.alter_column(u'information_news', 'body_en', self.gf('tinymce.models.HTMLField')(default=None))

    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['information.News']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'information.usefullinformaton': {
            'Meta': {'object_name': 'UsefullInformaton'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['information']