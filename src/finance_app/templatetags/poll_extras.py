from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
def lower1(value):
    new_value = str(value) + "  " * (20 - len(str(value)))
    new_value = f"{value}___"
    return new_value


@register.filter
def get_dict_item(target_dict, key):
    return target_dict.get(key, "")
