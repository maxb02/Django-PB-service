from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ActRequestForm

@login_required
def requestform(request):
    form = ActRequestForm
    return render(request, 'documents/request_form.html', {'form': form})