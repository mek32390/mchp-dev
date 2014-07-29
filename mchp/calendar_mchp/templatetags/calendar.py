from django.template import Library, Node
     
register = Library()
     
class WeekNode(Node):
    def render(self, context):
        context['week'] = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'] 
        return ''
    
@register.tag
def get_week(parser, token):
    return WeekNode()
