from modeltranslation.translator import translator, TranslationOptions
from models import Certificate


class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Certificate, CertificateTranslationOptions)
