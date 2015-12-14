# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'OfficeContact.rght'
        db.delete_column(u'contacts_officecontact', u'rght')

        # Deleting field 'OfficeContact.level'
        db.delete_column(u'contacts_officecontact', u'level')

        # Deleting field 'OfficeContact.tree_id'
        db.delete_column(u'contacts_officecontact', u'tree_id')

        # Deleting field 'OfficeContact.lft'
        db.delete_column(u'contacts_officecontact', u'lft')

        # Deleting field 'OfficeContact.id'
        db.delete_column(u'contacts_officecontact', u'id')

        # Adding field 'OfficeContact.contact_ptr'
        db.add_column(u'contacts_officecontact', u'contact_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['contacts.Contact'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'OfficeContact.rght'
        db.add_column(u'contacts_officecontact', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'OfficeContact.level'
        db.add_column(u'contacts_officecontact', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'OfficeContact.tree_id'
        db.add_column(u'contacts_officecontact', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'OfficeContact.lft'
        db.add_column(u'contacts_officecontact', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'OfficeContact.id'
        db.add_column(u'contacts_officecontact', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'OfficeContact.contact_ptr'
        db.delete_column(u'contacts_officecontact', u'contact_ptr_id')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'contacts.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.employee': {
            'Meta': {'object_name': 'Employee', '_ormbases': [u'contacts.Contact']},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'second_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'second_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'contacts.faxnumber': {
            'Meta': {'object_name': 'FaxNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'fax_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.officecontact': {
            'Meta': {'object_name': 'OfficeContact', '_ormbases': [u'contacts.Contact']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contacts.skypename': {
            'Meta': {'object_name': 'SkypeName'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skype_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contacts.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contacts']