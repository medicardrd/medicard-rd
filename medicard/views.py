from django.shortcuts import render
from .models import Medicard_rd
from django.contrib.auth.models import User
from .filters import UserFilter, UserFilterMedicard_rd
from django.contrib.sessions.models import Session


# Create your views here.
# 40222563765
# 40224716544

def inicio(request):
    return render(request, 'medicard/pagina_inicio.html', {})


def logout(request):
    return render(request, 'registration/logout.html')


def medio(request):
    Session.objects.all().delete()
    return render(request, 'registration/medio.html')


def historial(request, user=None):
    username = request.GET.get('username','no user')
    user_list = User.objects.filter(username = username)
    user_filter = UserFilter(request.GET, queryset=user_list)
    user_med = Medicard_rd.objects.filter(paciente = user_list)
    user_medicard = UserFilterMedicard_rd(request.GET, queryset=user_med)
    return render(request, 'medicard/historial.html', {'filter': user_filter, 'filter_2': user_medicard, 'User': username})


def search(request):
    user_list = User.objects.filter(perfil__rol=2)
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'medicard/user_list.html', {'filter': user_filter})
