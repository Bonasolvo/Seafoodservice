from modeltranslation.translator import translator, TranslationOptions
from models import Employee, OfficeContact


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('first_name', 'second_name', 'last_name', 'post',)

class OfficeContactOptions(TranslationOptions):
    fields = ('address',)

translator.register(OfficeContact, OfficeContactOptions)
translator.register(Employee, EmployeeTranslationOptions)

