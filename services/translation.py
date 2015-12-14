from modeltranslation.translator import translator, TranslationOptions
from models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Service, ServiceTranslationOptions)
