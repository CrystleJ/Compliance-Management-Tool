from django import template

register = template.Library()

@register.filter
def semi_colon_space(value):
    if value == None:
        return
    return value.replace(";","; ")

@register.simple_tag
def get_recommendation(cmmc_level, systems):
    if cmmc_level == None and systems == None:
        return ""
    return "YES"