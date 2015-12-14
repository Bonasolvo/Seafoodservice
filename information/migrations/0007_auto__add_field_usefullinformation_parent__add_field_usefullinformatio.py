# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UsefullInformation.parent'
        db.add_column(u'information_usefullinformation', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['information.UsefullInformation'], null=True),
                      keep_default=False)

        # Adding field 'UsefullInformation.lft'
        db.add_column(u'information_usefullinformation', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'UsefullInformation.rght'
        db.add_column(u'information_usefullinformation', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'UsefullInformation.tree_id'
        db.add_column(u'information_usefullinformation', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'UsefullInformation.level'
        db.add_column(u'information_usefullinformation', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UsefullInformation.parent'
        db.delete_column(u'information_usefullinformation', 'parent_id')

        # Deleting field 'UsefullInformation.lft'
        db.delete_column(u'information_usefullinformation', u'lft')

        # Deleting field 'UsefullInformation.rght'
        db.delete_column(u'information_usefullinformation', u'rght')

        # Deleting field 'UsefullInformation.tree_id'
        db.delete_column(u'information_usefullinformation', u'tree_id')

        # Deleting field 'UsefullInformation.level'
        db.delete_column(u'information_usefullinformation', u'level')


    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['information.News']", 'null': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'information.usefullinformation': {
            'Meta': {'object_name': 'UsefullInformation'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['information.UsefullInformation']", 'null': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['information']