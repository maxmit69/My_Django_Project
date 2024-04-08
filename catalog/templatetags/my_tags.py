from django import template

register = template.Library()


@register.filter()
def my_media(values):
    if values:
        return f'/media/{values}'

    return '#'
