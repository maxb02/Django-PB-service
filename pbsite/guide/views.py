from django.shortcuts import render

from django.views.generic import TemplateView

class GuideFormViev(TemplateView):
    template_name = 'guide/guide_form.html'
