from django.template import Library, Node

from schedule.utils import WEEK_DAYS
     
register = Library()
     
class WeekNode(Node):
    def render(self, context):
        context['week'] = WEEK_DAYS
        return ''
    
@register.tag
def get_week(parser, token):
    return WeekNode()
