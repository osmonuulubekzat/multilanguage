from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Bloggers)
class BloggersTranslationOptions(TranslationOptions):
    fields = ('name', 'text')



