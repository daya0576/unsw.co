from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    cats = Category.objects.order_by('-likes')[0:6]
    return {'cats': cats,  'act_cat': cat}

