from modeltranslation.translator import translator, TranslationOptions
from models import TransportationsGeography


class TransportationsTranslationOptions(TranslationOptions):
    fields = ('description', 'title')

translator.register(TransportationsGeography, TransportationsTranslationOptions)
