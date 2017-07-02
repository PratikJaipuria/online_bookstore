from django import template

register= template.Library()

@register.filter(name='tocents')
def tocents(value):
    return value * 100

@register.filter(name='pluralize')
def pluralize(value):
    retval = ""
    if value > 1:
        retval= "s"
    return retval