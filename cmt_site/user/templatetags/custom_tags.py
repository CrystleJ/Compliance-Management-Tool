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

@register.simple_tag
def get_add_edit(control_id):
    status = {"AC-1": "Not Applicable",
        "AC-10": "Not Compliant",
        "AC-5": "Compliant",
        "AC-6": "Compliant",
        "AT-2": "Compliant",
        "AU-2": "Not Compliant",
        "AU-3": "Not Compliant",
        "AU-6": "Not Applicable",
        "CM-2": "Compliant",
        "CM-8": "Compliant",
        "CP-9": "Compliant",
        "CP-10": "Compliant",
        "IA-2": "Compliant",
        "IA-5": "Compliant",        
        "PS-4": "Compliant",
        "PS-5": "Compliant",
        "RA-3": "Not Reviewed",
        "RA-5": "Not Reviewed",
        "SC-23": "Not Compliant",
        "SI-10": "Compliant",
    }

    if control_id in status:
        return "EDIT"
    
    return "ADD"

@register.simple_tag
def get_review_status(control_id):
    status = {"AC-1": "Not Applicable",
        "AC-10": "Not Compliant",
        "AC-5": "Compliant",
        "AC-6": "Compliant",
        "AT-2": "Compliant",
        "AU-2": "Not Compliant",
        "AU-3": "Not Compliant",
        "AU-6": "Not Applicable",
        "CM-2": "Compliant",
        "CM-8": "Compliant",
        "CP-9": "Compliant",
        "CP-10": "Compliant",
        "IA-2": "Compliant",
        "IA-5": "Compliant",        
        "PS-4": "Compliant",
        "PS-5": "Compliant",
        "RA-3": "Not Reviewed",
        "RA-5": "Not Reviewed",
        "SC-23": "Not Compliant",
        "SI-10": "Compliant",
    }

    if control_id in status:
        return status[control_id]
    
    return "Not Reviewed"