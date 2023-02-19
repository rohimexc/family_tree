from django import template
from django.contrib.auth.models import User
from family_app.models import Profile

register = template.Library()

@register.filter
def remove_negative(value):
    if value < 0:
        return abs(value)
    else:
        return value

