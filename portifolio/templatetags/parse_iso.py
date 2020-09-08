from django.template import Library
from datetime import datetime

register = Library()

@register.filter(expects_localtime=True)
def parse_iso(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")