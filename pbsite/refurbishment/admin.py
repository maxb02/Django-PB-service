from django.contrib import admin
from django import forms
from .models import RefurbishmentDevice, Defect, Refurbishment, Condition



admin.site.register(RefurbishmentDevice)
# admin.site.register(Refurbishment)
admin.site.register(Defect)
admin.site.register(Condition)

class RefurbishmentAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RefurbishmentAdminForm, self).__init__(*args, **kwargs)
        self.fields['prohibited_with'].queryset = Refurbishment.objects.exclude(id=self.instance.id)

@admin.register(Refurbishment)
class RefurbishmentAdmin(admin.ModelAdmin):
    form = RefurbishmentAdminForm



# class MyModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(MyModelAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user