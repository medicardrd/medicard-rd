from django.shortcuts import render
from .models import Medicard_rd
from django.contrib.auth.models import User
from .filters import UserFilter, UserFilterMedicard_rd
from . import models
from django.utils import timezone

# Create your views here.


def inicio(request):
    return render(request, 'medicard/pagina_inicio.html', {})
def logout(request):
    return render(request, 'registration/logout.html')

def historial(request):
    user_list = User.objects.filter(perfil__rol=2)
    user_med = Medicard_rd.objects.filter(paciente__perfil__rol=2)
    user_filter = UserFilter(request.GET, queryset=user_list)
    user_medicard = UserFilterMedicard_rd(request.GET, queryset=user_med)
    return render(request, 'medicard/historial.html', {'filter':user_filter, 'filter_2':user_medicard})


def search(request):
    user_list = User.objects.filter(perfil__rol=2)
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'medicard/user_list.html', {'filter': user_filter})
