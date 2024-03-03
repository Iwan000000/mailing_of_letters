from django import template

register = template.Library()

@register.filter
def my_media(val):
    """
    Этот тег для медиафайлов.
    """
    if val:
        return f'/media/{val}'
    else:
        return '#'
