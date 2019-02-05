from .models import Act

def documents_in_process(request):
    return {'documents_in_process': Act.objects.filter(status="in_process").count()}