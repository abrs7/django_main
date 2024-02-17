from django import template


register = template.Library()


def cut(value, arg):
    """
    This cuts out all values of 'args' from the strings!!
    
    """
    return value.replace(arg,'')

register.filter('cut',cut)