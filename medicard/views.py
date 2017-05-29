from django.shortcuts import render
from .models import Medicard_rd
from django.utils import timezone

# Create your views here.
def inicio(request):
    historial = Medicard_rd.objects.filter(fecha_creacion=timezone.now()).order_by('fecha_creacion')
    return render(request, 'medicard/pagina_inicio.html', {'historial': historial}) 