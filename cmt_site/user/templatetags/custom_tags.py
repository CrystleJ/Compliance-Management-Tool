from django import template

register = template.Library()

@register.filter
def semi_colon_space(value):
    if value == None:
        return
    return value.replace(";","; ")