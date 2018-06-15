from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News
from technicalguides.models import Guide

from users.models import User

@login_required
def index(request):
    news = News.objects.order_by('-published_date')
    groups_news = News.objects.for_user_groups(user=request.user)
    guides = Guide.objects.order_by('-published_date')
    groups_guides = Guide.objects.for_user_groups(user=request.user)



    return render(request, 'main/index.html', {'news': news,
                                                          'groups_news': groups_news,
                                               'groups_guides': groups_guides,
                                                          'guides': guides
                                               })