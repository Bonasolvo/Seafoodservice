# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VideoGallery.video_image'
        db.add_column(u'gallery_videogallery', 'video_image',
                      self.gf('django.db.models.FileField')(default='css\\images\\slide3.png', max_length=100),
                      keep_default=False)


        # Changing field 'VideoGallery.video'
        db.alter_column(u'gallery_videogallery', 'video', self.gf('django.db.models.FileField')(max_length=100))

        # Changing field 'PhotoGallery.photo'
        db.alter_column(u'gallery_photogallery', 'photo', self.gf('django.db.models.FileField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'VideoGallery.video_image'
        db.delete_column(u'gallery_videogallery', 'video_image')


        # Changing field 'VideoGallery.video'
        db.alter_column(u'gallery_videogallery', 'video', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'PhotoGallery.photo'
        db.alter_column(u'gallery_photogallery', 'photo', self.gf('django.db.models.fields.files.FileField')(max_length=100))

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
            'video': ('django.db.models.FileField', [], {'max_length': '100'}),
            'video_image': ('django.db.models.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gallery']