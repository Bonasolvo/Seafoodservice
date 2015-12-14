# coding: utf-8
from django.contrib import admin
from django import forms

from models import Email, Employee, SkypeName, TelephoneNumber

class EmailInline(admin.StackedInline):
    model = Email
    extra = 1

class SkypeInline(admin.StackedInline):
    model = SkypeName
    extra = 1

class TelephoneNumberInline(admin.StackedInline):
    model = TelephoneNumber
    extra = 1

class EmployeeForm(forms.ModelForm):
    first_name_ru = forms.CharField(required=True, )
    second_name_ru = forms.CharField(required=True, )
    last_name_ru = forms.CharField(required=True, )

    class Meta:
        model = Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'last_name', 'post','skypes', 'numbers', 'emails', ]
    search_fields = ['first_name_ru','first_name_en', 'second_name_ru', 'second_name_en', 'last_name_ru', 'last_name_en',]
    inlines = [TelephoneNumberInline, EmailInline, SkypeInline, ]
    form = EmployeeForm
    exclude = ['parent', 'first_name','second_name','last_name', 'post']

    @staticmethod
    def skypes(obj):
        skypes = SkypeName.objects.filter(employee=obj.id)
        return "" if not(skypes) else ", ".join(str(o) for o in skypes)

    @staticmethod
    def numbers(obj):
        numbers = TelephoneNumber.objects.filter(employee=obj.id)
        return "" if not(numbers) else ", ".join(str(o) for o in numbers)

    @staticmethod
    def emails(obj):
        emails = Email.objects.filter(employee=obj.id)
        return "" if not(emails) else ", ".join(str(o) for o in emails)

admin.site.register(Employee, EmployeeAdmin)