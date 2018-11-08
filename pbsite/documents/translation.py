from modeltranslation.translator import register, TranslationOptions
from .models import Accessory, VisualDefect


@register(Accessory)
class AccessoryTranslationOptions(TranslationOptions):
    fields = ('item',)

@register(VisualDefect)
class VisualDefectTranslationOptions(TranslationOptions):
    fields = ('defect',)