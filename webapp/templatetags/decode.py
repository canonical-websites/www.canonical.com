from django import template
import html

register = template.Library()

@register.filter(name='decode')
def decode(value):
    """HTML decodes a string """
    return html.unescape(value)
