from modeltranslation.translator import translator, TranslationOptions
from models import PhotoGallery, VideoGallery


class MediaTranslationOptions(TranslationOptions):
    fields = ('description', )


class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )

translator.register(PhotoGallery, PhotoTranslationOptions)
translator.register(VideoGallery, MediaTranslationOptions)