from atexit import register
from django import template

register = template.Library()

@register.simple_tag
def show_block(object, filter):
    ar = []
    arg = getattr(object, filter)
    print(arg.all())
    for i in arg.all():
        ar.append(i)

    #for i in ar:
    #    print(type(i))
    return ar

@register.filter
def get_obj(obj):
    print(obj.__class__.__name__)
    return str(obj.__class__.__name__)