from modeltranslation.translator import register, TranslationOptions
from .models import ScopeOfSupply, VisualDefect


@register(ScopeOfSupply)
class ScopeOfSupplyTranslationOptions(TranslationOptions):
    fields = ('item',)

@register(VisualDefect)
class VisualDefectTranslationOptions(TranslationOptions):
    fields = ('defect',)