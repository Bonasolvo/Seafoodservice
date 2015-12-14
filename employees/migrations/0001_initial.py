# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'employees_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Employee'], null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('first_name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('post_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'employees', ['Employee'])

        # Adding model 'TelephoneNumber'
        db.create_table(u'employees_telephonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Employee'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'employees', ['TelephoneNumber'])

        # Adding model 'Email'
        db.create_table(u'employees_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Employee'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'employees', ['Email'])

        # Adding model 'SkypeName'
        db.create_table(u'employees_skypename', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Employee'])),
            ('skype_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'employees', ['SkypeName'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'employees_employee')

        # Deleting model 'TelephoneNumber'
        db.delete_table(u'employees_telephonenumber')

        # Deleting model 'Email'
        db.delete_table(u'employees_email')

        # Deleting model 'SkypeName'
        db.delete_table(u'employees_skypename')


    models = {
        u'employees.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'employees.employee': {
            'Meta': {'object_name': 'Employee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Employee']", 'null': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'employees.skypename': {
            'Meta': {'object_name': 'SkypeName'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skype_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'employees.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['employees']