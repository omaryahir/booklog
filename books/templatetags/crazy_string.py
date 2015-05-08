from django import template
import random
register = template.Library()

@register.filter(name="crazy_string")
def crazy_string(string):
    string = list(str(string))
    random.shuffle(string)
    return "".join(string)
