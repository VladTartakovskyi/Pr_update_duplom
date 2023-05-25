from django.db.models import Count
from .models import *

menu = [{'title': "Головна", 'url_name': 'home'},
        {'title': "Про сайт", 'url_name': 'about'},
        {'title': "Добавити контент", 'url_name': 'add_page'},
        {'title': "Відгукнутись на вакансію", 'url_name': 'contact'},
        {'title': "Курси", 'url_name': 'cursu'},
        {'title': "Затребувані професії", 'url_name': 'proff'}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Profession.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
