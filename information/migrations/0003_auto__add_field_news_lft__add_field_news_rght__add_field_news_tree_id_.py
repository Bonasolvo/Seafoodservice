# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.lft'
        db.add_column(u'information_news', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'News.rght'
        db.add_column(u'information_news', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'News.tree_id'
        db.add_column(u'information_news', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'News.level'
        db.add_column(u'information_news', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.lft'
        db.delete_column(u'information_news', u'lft')

        # Deleting field 'News.rght'
        db.delete_column(u'information_news', u'rght')

        # Deleting field 'News.tree_id'
        db.delete_column(u'information_news', u'tree_id')

        # Deleting field 'News.level'
        db.delete_column(u'information_news', u'level')


    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
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