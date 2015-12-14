# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TransportationsGeography.lft'
        db.add_column(u'transporation_transportationsgeography', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'TransportationsGeography.rght'
        db.add_column(u'transporation_transportationsgeography', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'TransportationsGeography.tree_id'
        db.add_column(u'transporation_transportationsgeography', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'TransportationsGeography.level'
        db.add_column(u'transporation_transportationsgeography', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TransportationsGeography.lft'
        db.delete_column(u'transporation_transportationsgeography', u'lft')

        # Deleting field 'TransportationsGeography.rght'
        db.delete_column(u'transporation_transportationsgeography', u'rght')

        # Deleting field 'TransportationsGeography.tree_id'
        db.delete_column(u'transporation_transportationsgeography', u'tree_id')

        # Deleting field 'TransportationsGeography.level'
        db.delete_column(u'transporation_transportationsgeography', u'level')


    models = {
        u'transporation.transportationsgeography': {
            'Meta': {'object_name': 'TransportationsGeography'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['transporation']