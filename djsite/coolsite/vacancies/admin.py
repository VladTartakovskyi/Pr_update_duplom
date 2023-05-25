from urllib import request

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
# Register your models here.

from .models import *


class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'posada', 'firma', 'city', 'street', 'vumogu', 'responsibilities', 'time_create', 'pr')
    list_display_links = ('id', 'posada')
    search_fields = ('posada', 'city')

    def has_add_permission(self, request):
        return True if request.user.groups.filter(name='Вакансії').exists() else False

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return True if request.user.groups.filter(name='Вакансії').exists() else False
        return True

    def has_delete_permission(self, request, obj=None):
        return True if request.user.groups.filter(name='Вакансії').exists() else False


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class UnemployedAdmin(admin.ModelAdmin):
    list_display = ('id', 'priz', 'name', 'pobat', 'city', 'street', 'year', 'nomer_phone', 'special', 'rez')
    list_display_links = ('id', 'priz')
    search_fields = ('priz', )

class CurseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pip_v', 'truvalist', 'city', 'adress', 'pr', 'vartist')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'city')




admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Unemployed, UnemployedAdmin)
admin.site.register(Cursu, CurseAdmin)
admin.site.register(Category, CategoryAdmin)

