from django import template
from vacancies.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_profession(filter=None):
    if not filter:
         return Profession.objects.all()
    else:
        return Profession.objects.filter(pk=filter)

@register.simple_tag(name='getct')
def get_category(filter=None):
    if not filter:
         return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('vacancies/list_categories.html')
def show_profession(sort:None, cat_selected=0):
    if not sort:
        cats = Profession.objects.all()
    else:
        cats = Profession.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

@register.inclusion_tag('vacancies/list_categories_cursu.html')
def show_category(sort:None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}