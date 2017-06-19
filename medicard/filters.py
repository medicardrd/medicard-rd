from django.contrib.auth.models import User
import django_filters

from medicard.models import Medicard_rd


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', ]# 'first_name', 'last_name', ]

class UserFilterMedicard_rd(django_filters.FilterSet):
    class Meta:
        model = Medicard_rd
        fields = ['paciente', ]# 'first_name', 'last_name', ]