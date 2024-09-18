from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter(name='replace_spaces')
def replace_spaces(value):
    return value.replace(' ', '-')

@register.filter(name='slugify')
def slugify_filter(value):
    return slugify(value)
