from django import template
from abonement.models import *

register = template.Library()


@register.inclusion_tag('abonement/menu.html', name='menu')
def show_menu():
    menu = [{'title': 'Make an appointment', 'url_name': 'new_training'},
            {'title': 'Group trainings', 'url_name': 'group_schedule'},
            {'title': 'Examinations', 'url_name': 'examination'},
            {'title': 'Profile', 'url_name': 'profile'}]
    return {"menu": menu}
