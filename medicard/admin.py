from django.contrib import admin
from .models import Medicard_rd
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import perfil

class ProfileInline(admin.StackedInline):
    model = perfil
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class Medicard_rdAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['paciente'].queryset = User.objects.filter(perfil__rol ='2')
         context['adminform'].form.fields['doctor'].queryset = User.objects.filter(perfil__rol='1')
         return super(Medicard_rdAdmin, self).render_change_form(request, context, args, kwargs)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Medicard_rd, Medicard_rdAdmin)
admin.site.site_title = 'MedicardRD Administration'
admin.site.site_header = 'Medicard RD authentication'
