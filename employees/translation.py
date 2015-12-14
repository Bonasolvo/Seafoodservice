from modeltranslation.translator import translator, TranslationOptions
from models import Employee


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('first_name', 'second_name', 'last_name', 'post',)

translator.register(Employee, EmployeeTranslationOptions)

