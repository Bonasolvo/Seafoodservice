from modeltranslation.translator import translator, TranslationOptions
from information.models import News, UsefullInformation, MainPage


class InformationTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(News, InformationTranslationOptions)
translator.register(UsefullInformation, InformationTranslationOptions)

class MainPageTranslationOptions(TranslationOptions):
    fields = ( 'body',)

translator.register(MainPage, MainPageTranslationOptions)