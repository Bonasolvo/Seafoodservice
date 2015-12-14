# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'VideoGallery.video'
        db.delete_column(u'gallery_videogallery', 'video')

        # Deleting field 'VideoGallery.type'
        db.delete_column(u'gallery_videogallery', 'type')


    def backwards(self, orm):
        # Adding field 'VideoGallery.video'
        db.add_column(u'gallery_videogallery', 'video',
                      self.gf('django.db.models.FileField')(default=None, max_length=100),
                      keep_default=False)

        # Adding field 'VideoGallery.type'
        db.add_column(u'gallery_videogallery', 'type',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=15),
                      keep_default=False)


    models = {
        u'gallery.photogallery': {
            'Meta': {'object_name': 'PhotoGallery'},
            'add_this_photo_to_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'add_this_photo_to_slide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related'", 'null': 'True', 'to': u"orm['gallery.PhotoGallery']"}),
            'photo': ('django.db.models.FileField', [], {'max_length': '100'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'gallery.videogallery': {
            'Meta': {'object_name': 'VideoGallery'},
            'add_this_photo_to_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related'", 'null': 'True', 'to': u"orm['gallery.VideoGallery']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'video_image': ('django.db.models.FileField', [], {'default': "'css/images/slide3.png'", 'max_length': '100'})
        }
    }

    complete_apps = ['gallery']