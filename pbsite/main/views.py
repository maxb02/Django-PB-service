from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News
from technicalguides.models import Guide


@login_required
def index(request):
    if request.user.is_staff:
        news = News.objects.order_by('-published_date')
        guides = Guide.objects.order_by('-published_date')
    else:
        news = News.objects.filter(group__in=request.user.groups.all()).order_by('-published_date')
        guides = Guide.objects.filter(group__in=request.user.groups.all()).order_by('-published_date')

    return render(request, 'main/index.html', {'news': news,
                                               'guides': guides
                                               })
