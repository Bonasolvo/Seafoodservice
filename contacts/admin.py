# coding: utf-8
from django.contrib import admin
from django import forms

from models import *

class EmailInline(admin.StackedInline):
    model = Email
    extra = 1

class SkypeInline(admin.StackedInline):
    model = SkypeName
    extra = 1

class TelephoneNumberInline(admin.StackedInline):
    model = TelephoneNumber
    extra = 1

class FaxNumberInline(admin.StackedInline):
    model = FaxNumber
    extra = 1

class EmployeeForm(forms.ModelForm):
    first_name_ru = forms.CharField(required=True, label=u'Имя')
    first_name_en = forms.CharField(required=False, label=u'Имя (en)')
    second_name_ru = forms.CharField(required=True, label=u'Отчество')
    second_name_en = forms.CharField(required=False, label=u'Отчество (en)')
    last_name_ru = forms.CharField(required=True, label=u'Фамилия')
    last_name_en = forms.CharField(required=False, label=u'Фамлия (en)')

    class Meta:
        model = Employee


class OfficeContactForm(forms.ModelForm):
    address_ru = forms.CharField(required=True, )
    address_en = forms.CharField(required=False, )

    class Meta:
        model = OfficeContact

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'second_name', 'last_name', 'post','skypes', 'numbers', 'emails', ]
    search_fields = ['first_name_ru','first_name_en', 'second_name_ru', 'second_name_en', 'last_name_ru', 'last_name_en',]
    inlines = [TelephoneNumberInline, EmailInline, SkypeInline, ]
    form = EmployeeForm
    exclude = ['parent', 'first_name','second_name','last_name', 'post']

    @staticmethod
    def skypes(obj):
        skypes = SkypeName.objects.filter(contact=obj.id)
        return "" if not(skypes) else ", ".join(str(o) for o in skypes)

    @staticmethod
    def numbers(obj):
        numbers = TelephoneNumber.objects.filter(contact=obj.id)
        return "" if not(numbers) else ", ".join(str(o) for o in numbers)

    @staticmethod
    def emails(obj):
        emails = Email.objects.filter(contact=obj.id)
        return "" if not(emails) else ", ".join(str(o) for o in emails)


class OfficeContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'faxs', 'skypes', 'numbers', 'emails', ]
    search_fields = ['address_ru', 'address_en']
    inlines = [TelephoneNumberInline, EmailInline, SkypeInline, FaxNumberInline ]
    form = OfficeContactForm
    exclude = ['parent', 'address',]

    @staticmethod
    def skypes(obj):
        skypes = SkypeName.objects.filter(contact=obj.id)
        return "" if not(skypes) else ", ".join(str(o) for o in skypes)

    @staticmethod
    def numbers(obj):
        numbers = TelephoneNumber.objects.filter(contact=obj.id)
        return "" if not(numbers) else ", ".join(str(o) for o in numbers)

    @staticmethod
    def emails(obj):
        emails = Email.objects.filter(contact=obj.id)
        return "" if not(emails) else ", ".join(str(o) for o in emails)

    @staticmethod
    def faxs(obj):
        faxs = FaxNumber.objects.filter(contact=obj.id)
        return "" if not(faxs) else ", ".join(str(o) for o in faxs)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'email', 'user_message']
    search_fields = ['name', 'number', 'email', 'message']

    def user_message(self, obj):
        return obj.message[0:30]

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(OfficeContact, OfficeContactAdmin)
admin.site.register(Message, MessageAdmin)