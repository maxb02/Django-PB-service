from django import template
from django.contrib.auth.models import Group
from technicalguides.models import Guide
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
#
# @register.filter(name='guide_group')
# def guide_group(user, guide):
#     if set((user.groups.all()) guide.group.all())
#     return True if group in user.groups.all() else False