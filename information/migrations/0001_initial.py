# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'information_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body_en', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'information', ['News'])

        # Adding model 'UsefullInformaton'
        db.create_table(u'information_usefullinformaton', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body_en', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'information', ['UsefullInformaton'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'information_news')

        # Deleting model 'UsefullInformaton'
        db.delete_table(u'information_usefullinformaton')


    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'})
        },
        u'information.usefullinformaton': {
            'Meta': {'object_name': 'UsefullInformaton'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['information']